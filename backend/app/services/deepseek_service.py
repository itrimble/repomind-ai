from openai import OpenAI
from dotenv import load_dotenv
from app.utils.format_message import format_user_message
import tiktoken
import os
import aiohttp
import json
from typing import AsyncGenerator, Literal

load_dotenv()


class DeepSeekService:
    def __init__(self):
        self.default_client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url="https://api.deepseek.com/v1"
        )
        # Use the same encoding as OpenAI for token counting compatibility
        self.encoding = tiktoken.get_encoding("o200k_base")
        self.base_url = "https://api.deepseek.com/v1/chat/completions"

    def call_deepseek_api(
        self,
        system_prompt: str,
        data: dict,
        api_key: str | None = None,
        model: str = "deepseek-chat",
    ) -> str:
        """
        Makes an API call to DeepSeek and returns the response.

        Args:
            system_prompt (str): The instruction/system prompt
            data (dict): Dictionary of variables to format into the user message
            api_key (str | None): Optional custom API key
            model (str): DeepSeek model to use

        Returns:
            str: DeepSeek's response text
        """
        # Create the user message with the data
        user_message = format_user_message(data)

        # Use custom client if API key provided, otherwise use default
        client = OpenAI(
            api_key=api_key or os.getenv("DEEPSEEK_API_KEY"),
            base_url="https://api.deepseek.com/v1"
        ) if api_key else self.default_client

        try:
            print(
                f"Making non-streaming API call to DeepSeek with API key: {'custom key' if api_key else 'default key'}"
            )

            completion = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message},
                ],
                max_tokens=8000,
                temperature=0,
            )

            return completion.choices[0].message.content

        except Exception as e:
            print(f"Error in call_deepseek_api: {str(e)}")
            raise e

    async def call_deepseek_api_stream(
        self,
        system_prompt: str,
        data: dict,
        api_key: str | None = None,
        model: str = "deepseek-chat",
    ) -> AsyncGenerator[str, None]:
        """
        Makes a streaming API call to DeepSeek and yields response chunks.

        Args:
            system_prompt (str): The instruction/system prompt
            data (dict): Dictionary of variables to format into the user message
            api_key (str | None): Optional custom API key
            model (str): DeepSeek model to use

        Yields:
            str: Chunks of DeepSeek's response
        """
        # Create the user message with the data
        user_message = format_user_message(data)

        headers = {
            "Authorization": f"Bearer {api_key or os.getenv('DEEPSEEK_API_KEY')}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ],
            "max_tokens": 8000,
            "temperature": 0,
            "stream": True,
        }

        try:
            print(f"Making streaming API call to DeepSeek")
            
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.base_url, headers=headers, json=payload
                ) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        raise Exception(f"DeepSeek API error: {response.status} - {error_text}")

                    async for line in response.content:
                        line = line.decode("utf-8").strip()
                        if line.startswith("data: "):
                            data_content = line[6:]
                            if data_content == "[DONE]":
                                break
                            try:
                                chunk_data = json.loads(data_content)
                                if (
                                    "choices" in chunk_data
                                    and len(chunk_data["choices"]) > 0
                                    and "delta" in chunk_data["choices"][0]
                                    and "content" in chunk_data["choices"][0]["delta"]
                                ):
                                    content = chunk_data["choices"][0]["delta"]["content"]
                                    if content:
                                        yield content
                            except json.JSONDecodeError:
                                continue

        except Exception as e:
            print(f"Error in call_deepseek_api_stream: {str(e)}")
            raise e

    def count_tokens(self, text: str) -> int:
        """
        Count tokens in text using the encoding.

        Args:
            text (str): Text to count tokens for

        Returns:
            int: Number of tokens
        """
        return len(self.encoding.encode(text))
