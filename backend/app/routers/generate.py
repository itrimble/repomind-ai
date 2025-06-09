from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import StreamingResponse
from dotenv import load_dotenv
from app.services.github_service import GitHubService
from app.services.o4_mini_openai_service import OpenAIo4Service
from app.services.deepseek_service import DeepSeekService
from app.prompts import (
    SYSTEM_FIRST_PROMPT,
    SYSTEM_SECOND_PROMPT,
    SYSTEM_THIRD_PROMPT,
    ADDITIONAL_SYSTEM_INSTRUCTIONS_PROMPT,
)
from anthropic._exceptions import RateLimitError
from pydantic import BaseModel
from functools import lru_cache
import re
import json
import asyncio
import os

# from app.services.claude_service import ClaudeService
# from app.core.limiter import limiter

load_dotenv()

router = APIRouter(prefix="/generate", tags=["DeepSeek & OpenAI"])

# Initialize services
# claude_service = ClaudeService()
o4_service = OpenAIo4Service()
deepseek_service = DeepSeekService()


# cache github data to avoid double API calls from cost and generate
@lru_cache(maxsize=100)
def get_cached_github_data(username: str, repo: str, github_pat: str | None = None):
    # Create a new service instance for each call with the appropriate PAT
    current_github_service = GitHubService(pat=github_pat)

    default_branch = current_github_service.get_default_branch(username, repo)
    if not default_branch:
        default_branch = "main"  # fallback value

    file_tree = current_github_service.get_github_file_paths_as_list(username, repo)
    readme = current_github_service.get_github_readme(username, repo)

    return {"default_branch": default_branch, "file_tree": file_tree, "readme": readme}


class ApiRequest(BaseModel):
    username: str
    repo: str
    instructions: str = ""
    api_key: str | None = None
    github_pat: str | None = None


@router.post("/cost")
# @limiter.limit("5/minute") # TEMP: disable rate limit for growth??
async def get_generation_cost(request: Request, body: ApiRequest):
    try:
        # Get file tree and README content
        github_data = get_cached_github_data(body.username, body.repo, body.github_pat)
        file_tree = github_data["file_tree"]
        readme = github_data["readme"]

        # Calculate combined token count using DeepSeek service
        file_tree_tokens = deepseek_service.count_tokens(file_tree)
        readme_tokens = deepseek_service.count_tokens(readme)
        total_tokens = file_tree_tokens * 2 + readme_tokens + 3000

        # Check if we should use DeepSeek or OpenAI based on context length
        use_deepseek = total_tokens > 150000  # Use DeepSeek for large repos
        
        if use_deepseek:
            # DeepSeek pricing (much cheaper and larger context)
            # Input cost: ~$0.14 per 1M tokens ($0.00000014 per token)
            # Output cost: ~$0.28 per 1M tokens ($0.00000028 per token)
            input_cost = total_tokens * 0.00000014
            output_cost = 8000 * 0.00000028
            estimated_cost = input_cost + output_cost
            provider = "DeepSeek"
        else:
            # OpenAI o4-mini pricing
            # Input cost: $1.1 per 1M tokens ($0.0000011 per token)
            # Output cost: $4.4 per 1M tokens ($0.0000044 per token)
            input_cost = total_tokens * 0.0000011
            output_cost = 8000 * 0.0000044
            estimated_cost = input_cost + output_cost
            provider = "OpenAI o4-mini"

        # Format as currency string
        cost_string = f"${estimated_cost:.4f} USD ({provider})"
        return {
            "cost": cost_string, 
            "provider": provider,
            "token_count": total_tokens,
            "use_deepseek": use_deepseek
        }
    except Exception as e:
        return {"error": str(e)}


def process_click_events(diagram: str, username: str, repo: str, branch: str) -> str:
    """
    Process click events in Mermaid diagram to include full GitHub URLs.
    Detects if path is file or directory and uses appropriate URL format.
    """

    def replace_path(match):
        # Extract the path from the click event
        path = match.group(2).strip("\"'")

        # Determine if path is likely a file (has extension) or directory
        is_file = "." in path.split("/")[-1]

        # Construct GitHub URL
        base_url = f"https://github.com/{username}/{repo}"
        path_type = "blob" if is_file else "tree"
        full_url = f"{base_url}/{path_type}/{branch}/{path}"

        # Return the full click event with the new URL
        return f'click {match.group(1)} "{full_url}"'

    # Match click events: click ComponentName "path/to/something"
    click_pattern = r'click ([^\s"]+)\s+"([^"]+)"'
    return re.sub(click_pattern, replace_path, diagram)


@router.post("/stream")
async def generate_stream(request: Request, body: ApiRequest):
    try:
        # Initial validation checks
        if len(body.instructions) > 1000:
            return {"error": "Instructions exceed maximum length of 1000 characters"}

        if body.repo in [
            "fastapi",
            "streamlit",
            "flask",
            "api-analytics",
            "monkeytype",
        ]:
            return {"error": "Example repos cannot be regenerated"}

        async def event_generator():
            try:
                # Get cached github data
                github_data = get_cached_github_data(
                    body.username, body.repo, body.github_pat
                )
                default_branch = github_data["default_branch"]
                file_tree = github_data["file_tree"]
                readme = github_data["readme"]

                # Send initial status
                yield f"data: {json.dumps({'status': 'started', 'message': 'Starting generation process...'})}\n\n"
                await asyncio.sleep(0.1)

                # Token count check and service selection
                combined_content = f"{file_tree}\n{readme}"
                token_count = deepseek_service.count_tokens(combined_content)
                
                # Determine which service to use based on token count
                use_deepseek = token_count > 150000
                service = deepseek_service if use_deepseek else o4_service
                service_name = "DeepSeek" if use_deepseek else "OpenAI o4-mini"
                
                # Updated limits for DeepSeek (much larger context window)
                max_tokens = 1000000 if use_deepseek else 195000  # DeepSeek can handle ~1M tokens
                wallet_limit = 500000 if use_deepseek else 50000  # Higher limit for DeepSeek due to lower cost

                if wallet_limit < token_count < max_tokens and not body.api_key and not use_deepseek:
                    yield f"data: {json.dumps({'error': f'File tree and README combined exceeds token limit ({wallet_limit:,}). Current size: {token_count:,} tokens. This GitHub repository is too large for my wallet, but you can continue by providing your own OpenAI API key or the system will automatically use DeepSeek for large repositories.'})}\n\n"
                    return
                elif token_count > max_tokens:
                    yield f"data: {json.dumps({'error': f'Repository is too large (>{max_tokens//1000}k tokens) for analysis. {service_name} max context length exceeded. Current size: {token_count:,} tokens.'})}\n\n"
                    return

                # Notify user which service is being used
                yield f"data: {json.dumps({'status': 'service_selected', 'message': f'Using {service_name} for this repository ({token_count:,} tokens)'})}\n\n"
                await asyncio.sleep(0.1)

                # Prepare prompts
                first_system_prompt = SYSTEM_FIRST_PROMPT
                third_system_prompt = SYSTEM_THIRD_PROMPT
                if body.instructions:
                    first_system_prompt = (
                        first_system_prompt
                        + "\n"
                        + ADDITIONAL_SYSTEM_INSTRUCTIONS_PROMPT
                    )
                    third_system_prompt = (
                        third_system_prompt
                        + "\n"
                        + ADDITIONAL_SYSTEM_INSTRUCTIONS_PROMPT
                    )

                # Phase 1: Get explanation
                yield f"data: {json.dumps({'status': 'explanation_sent', 'message': f'Sending explanation request to {service_name}...'})}\n\n"
                await asyncio.sleep(0.1)
                yield f"data: {json.dumps({'status': 'explanation', 'message': 'Analyzing repository structure...'})}\n\n"
                explanation = ""
                
                if use_deepseek:
                    async for chunk in service.call_deepseek_api_stream(
                        system_prompt=first_system_prompt,
                        data={
                            "file_tree": file_tree,
                            "readme": readme,
                            "instructions": body.instructions,
                        },
                        api_key=body.api_key,
                    ):
                        explanation += chunk
                        yield f"data: {json.dumps({'status': 'explanation_chunk', 'chunk': chunk})}\n\n"
                else:
                    async for chunk in service.call_o4_api_stream(
                        system_prompt=first_system_prompt,
                        data={
                            "file_tree": file_tree,
                            "readme": readme,
                            "instructions": body.instructions,
                        },
                        api_key=body.api_key,
                        reasoning_effort="medium",
                    ):
                        explanation += chunk
                        yield f"data: {json.dumps({'status': 'explanation_chunk', 'chunk': chunk})}\n\n"

                if "BAD_INSTRUCTIONS" in explanation:
                    yield f"data: {json.dumps({'error': 'Invalid or unclear instructions provided'})}\n\n"
                    return

                # Phase 2: Get component mapping
                yield f"data: {json.dumps({'status': 'mapping_sent', 'message': f'Sending component mapping request to {service_name}...'})}\n\n"
                await asyncio.sleep(0.1)
                yield f"data: {json.dumps({'status': 'mapping', 'message': 'Creating component mapping...'})}\n\n"
                full_second_response = ""
                
                if use_deepseek:
                    async for chunk in service.call_deepseek_api_stream(
                        system_prompt=SYSTEM_SECOND_PROMPT,
                        data={"explanation": explanation, "file_tree": file_tree},
                        api_key=body.api_key,
                    ):
                        full_second_response += chunk
                        yield f"data: {json.dumps({'status': 'mapping_chunk', 'chunk': chunk})}\n\n"
                else:
                    async for chunk in service.call_o4_api_stream(
                        system_prompt=SYSTEM_SECOND_PROMPT,
                        data={"explanation": explanation, "file_tree": file_tree},
                        api_key=body.api_key,
                        reasoning_effort="low",
                    ):
                        full_second_response += chunk
                        yield f"data: {json.dumps({'status': 'mapping_chunk', 'chunk': chunk})}\n\n"

                # i dont think i need this anymore? but keep it here for now
                # Extract component mapping
                start_tag = "<component_mapping>"
                end_tag = "</component_mapping>"
                component_mapping_text = full_second_response[
                    full_second_response.find(start_tag) : full_second_response.find(
                        end_tag
                    )
                ]

                # Phase 3: Generate Mermaid diagram
                yield f"data: {json.dumps({'status': 'diagram_sent', 'message': f'Sending diagram generation request to {service_name}...'})}\n\n"
                await asyncio.sleep(0.1)
                yield f"data: {json.dumps({'status': 'diagram', 'message': 'Generating diagram...'})}\n\n"
                mermaid_code = ""
                
                if use_deepseek:
                    async for chunk in service.call_deepseek_api_stream(
                        system_prompt=third_system_prompt,
                        data={
                            "explanation": explanation,
                            "component_mapping": component_mapping_text,
                            "instructions": body.instructions,
                        },
                        api_key=body.api_key,
                    ):
                        mermaid_code += chunk
                        yield f"data: {json.dumps({'status': 'diagram_chunk', 'chunk': chunk})}\n\n"
                else:
                    async for chunk in service.call_o4_api_stream(
                        system_prompt=third_system_prompt,
                        data={
                            "explanation": explanation,
                            "component_mapping": component_mapping_text,
                            "instructions": body.instructions,
                        },
                        api_key=body.api_key,
                        reasoning_effort="low",
                    ):
                        mermaid_code += chunk
                        yield f"data: {json.dumps({'status': 'diagram_chunk', 'chunk': chunk})}\n\n"

                # Process final diagram
                mermaid_code = mermaid_code.replace("```mermaid", "").replace("```", "")
                if "BAD_INSTRUCTIONS" in mermaid_code:
                    yield f"data: {json.dumps({'error': 'Invalid or unclear instructions provided'})}\n\n"
                    return

                processed_diagram = process_click_events(
                    mermaid_code, body.username, body.repo, default_branch
                )

                # Send final result
                yield f"data: {json.dumps({
                    'status': 'complete',
                    'diagram': processed_diagram,
                    'explanation': explanation,
                    'mapping': component_mapping_text
                })}\n\n"

            except Exception as e:
                yield f"data: {json.dumps({'error': str(e)})}\n\n"

        return StreamingResponse(
            event_generator(),
            media_type="text/event-stream",
            headers={
                "X-Accel-Buffering": "no",  # Hint to Nginx
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
            },
        )
    except Exception as e:
        return {"error": str(e)}
