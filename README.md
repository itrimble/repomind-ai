# 🧠 RepoMind AI (GitDiagram)

[![Image](./docs/readme_img.png "GitDiagram Front Page")](https://gitdiagram.com/)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
[![Kofi](https://img.shields.io/badge/Kofi-F16061.svg?logo=ko-fi&logoColor=white)](https://ko-fi.com/ahmedkhaleel2004)
![Next.js](https://img.shields.io/badge/Next.js-15.3.3-black) ![TypeScript](https://img.shields.io/badge/TypeScript-5.5.3-blue) ![Three.js](https://img.shields.io/badge/Three.js-Interactive%20Graphics-red)
![MCP](https://img.shields.io/badge/MCP-Enabled-purple) ![Claude](https://img.shields.io/badge/Claude-Enhanced-orange)

Turn any GitHub repository into an interactive diagram for visualization in seconds. Now with enhanced debugging capabilities, modern development tools, and full MCP (Model Context Protocol) integration for AI-assisted development.

You can also replace `hub` with `diagram` in any Github URL to access its diagram.

## 🚀 Features

### 🎯 Core Capabilities
- 👀 **Instant Visualization**: Convert any GitHub repository structure into a system design / architecture diagram
- 🎨 **Interactivity**: Click on components to navigate directly to source files and relevant directories
- ⚡ **Fast Generation**: Powered by DeepSeek AI for quick and accurate diagrams
- 🔄 **Customization**: Modify and regenerate diagrams with custom instructions
- 🌐 **API Access**: Public API available for integration
- 🎮 **3D Interactive Experience** - Three.js-powered immersive code exploration
- 📱 **Responsive Design** - Works seamlessly across all devices

### 🛠 Enhanced Development Features
- **🔧 Full Debugging Suite** - Comprehensive VS Code and browser debugging
- **🏗 Modern Architecture** - Next.js 15 with App Router and TypeScript
- **🎨 Enhanced UI/UX** - ShadCN UI components with Tailwind styling
- **📈 Performance Optimized** - Turbo mode and optimized rendering
- **🌙 Dark/Light Mode** - Theme switching with next-themes
- **🔒 Type-Safe Development** - Full TypeScript implementation

### 🤖 MCP Integration Features
- **🔌 Model Context Protocol** - Direct integration with Claude and other AI assistants
- **📋 Context-Aware Analysis** - AI understands your project structure automatically
- **🚀 Automated Development** - AI-assisted code generation and refactoring
- **🔍 Intelligent Code Review** - Automated analysis and suggestions
- **📊 Real-time Insights** - Live repository metrics and health monitoring
- **🎯 Smart Debugging** - AI-powered error detection and resolution

## ⚙️ Tech Stack

### Frontend Stack
- **Next.js 15.3.3** - React framework with App Router
- **TypeScript 5.5.3** - Type-safe development
- **Three.js** - 3D graphics and interactive visualizations
- **ShadCN UI** - Modern, accessible component library
- **Tailwind CSS** - Utility-first styling
- **Framer Motion** - Smooth animations and transitions

### Backend Stack
- **Python 3.13** - Backend API services
- **FastAPI** - High-performance API framework
- **PostgreSQL** - Primary database with Drizzle ORM
- **DeepSeek AI** - AI-powered code analysis (previously OpenAI)
- **Docker** - Containerized deployment

### Development Tools
- **VS Code/Cursor** - Enhanced debugging support
- **pnpm 9.13.0** - Fast, efficient package management
- **ESLint + Prettier** - Code quality and formatting
- **Turbo** - Accelerated development builds

### MCP Integration Stack
- **Model Context Protocol** - Direct AI assistant integration
- **Claude Sonnet 4** - Advanced code analysis and generation
- **Context-aware tooling** - Intelligent development assistance
- **Real-time collaboration** - AI-human collaborative development

## 🤖 MCP (Model Context Protocol) Integration

RepoMind AI is designed to work seamlessly with MCP-enabled AI assistants like Claude, providing intelligent development assistance directly within your workflow.

### 🔌 MCP Server Setup

#### Prerequisites
- Claude Desktop with MCP support
- Node.js 18.17+
- Valid GitHub Personal Access Token
- DeepSeek API key

#### Installation via Claude MCP

1. **Enable MCP in Claude Desktop:**
   ```json
   // Add to Claude MCP configuration
   {
     "mcpServers": {
       "repomind-ai": {
         "command": "npx",
         "args": ["@repomind/mcp-server"],
         "env": {
           "GITHUB_TOKEN": "your_github_token",
           "DEEPSEEK_API_KEY": "your_deepseek_api_key"
         }
       }
     }
   }
   ```

2. **Install MCP Server Package:**
   ```bash
   npm install -g @repomind/mcp-server
   ```

3. **Configure Environment:**
   ```bash
   # Create MCP configuration
   echo "GITHUB_TOKEN=your_token_here" >> ~/.repomind-mcp
   echo "DEEPSEEK_API_KEY=your_key_here" >> ~/.repomind-mcp
   ```

### 🎯 MCP Usage Examples

#### Repository Analysis
```
Ask Claude: "Analyze the architecture of facebook/react using RepoMind"
```
Claude will:
- Generate interactive repository diagram
- Provide architectural insights
- Suggest optimization opportunities
- Identify code patterns and issues

#### Code Generation
```
Ask Claude: "Generate a Next.js component similar to the patterns in vercel/next.js"
```
Claude will:
- Analyze Next.js repository structure
- Extract common patterns
- Generate type-safe components
- Follow established conventions

#### Debugging Assistance
```
Ask Claude: "Help debug performance issues in my Three.js application using RepoMind patterns"
```
Claude will:
- Analyze Three.js implementations
- Compare with best practices
- Suggest performance optimizations
- Provide working code examples

### 🛠 Available MCP Tools

#### Repository Tools
- `analyze_repository` - Deep repository analysis
- `generate_diagram` - Create interactive diagrams
- `extract_patterns` - Identify code patterns
- `compare_projects` - Cross-repository comparison

#### Development Tools
- `suggest_improvements` - AI-powered code suggestions
- `generate_tests` - Automated test generation
- `refactor_code` - Intelligent refactoring
- `optimize_performance` - Performance optimization

#### Integration Tools
- `sync_with_github` - Real-time GitHub integration
- `track_changes` - Monitor repository evolution
- `analyze_dependencies` - Dependency analysis
- `security_audit` - Security vulnerability detection

### 📊 MCP Configuration Options

```typescript
interface MCPConfig {
  // API Configuration
  deepseekApiKey: string;
  githubToken: string;
  
  // Analysis Settings
  maxDepth: number;          // Default: 3
  includeTests: boolean;     // Default: true
  analyzeDependencies: boolean; // Default: true
  
  // Output Preferences
  diagramFormat: 'mermaid' | 'plantuml' | 'graphviz';
  includeMetrics: boolean;
  generateInsights: boolean;
  
  // Integration Settings
  autoSync: boolean;         // Default: false
  webhookUrl?: string;
  slackIntegration?: boolean;
}
```

## 🚦 Quick Start

### Prerequisites
- Node.js 18.17+ 
- pnpm 9.13.0+
- Python 3.13+
- PostgreSQL 14+
- Docker (optional)

### 1. Clone & Install
```bash
git clone https://github.com/itrimble/repomind-ai.git
cd repomind-ai
pnpm install
```

### 2. Environment Setup
```bash
cp .env.example .env
# Edit .env with your configuration
```

Required environment variables:
```env
# Database
DATABASE_URL="postgresql://username:password@localhost:5432/repomind"

# AI Service
DEEPSEEK_API_KEY="your_deepseek_api_key"

# GitHub (for private repos)
GITHUB_TOKEN="your_github_token"

# MCP Integration
MCP_SERVER_PORT="3001"
MCP_ENABLE_WEBSOCKET="true"

# Analytics (optional)
POSTHOG_KEY="your_posthog_key"
```

### 3. Database Setup
```bash
# Start database (using provided script)
chmod +x start-database.sh
./start-database.sh

# Run migrations
pnpm run db:push

# Optional: Open database studio
pnpm run db:studio
```

### 4. Start Development
```bash
# Frontend (port 6002)
pnpm run dev

# Backend API (port 8000)
docker-compose up --build -d

# MCP Server (port 3001)
pnpm run mcp:start

# Check backend logs
docker-compose logs -f
```

### 5. Access Application
- **Frontend**: http://localhost:6002
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **MCP Server**: http://localhost:3001
- **Database Studio**: http://localhost:5555 (when running)

## 🐛 Enhanced Debugging Guide

This project now includes comprehensive debugging capabilities for modern development:

### VS Code Debugging (New!)
1. Open project in VS Code: `code .`
2. Go to Debug panel (`⇧+⌘+D`)
3. Select configuration:
   - **"Next.js: debug server-side"** - Server components & API routes
   - **"Next.js: debug client-side"** - React components (Chrome)
   - **"Next.js: debug client-side (Firefox)"** - React components (Firefox)
   - **"Next.js: debug full stack"** - Complete debugging experience
   - **"MCP Server: debug"** - Debug MCP integration
4. Press `F5` to start debugging
5. Set breakpoints and debug in real-time!

### Debug Scripts
```bash
# Server-side debugging with Node inspector
pnpm run dev:debug

# MCP server debugging
pnpm run mcp:debug

# Regular development (Turbo mode)
pnpm run dev

# Production debugging (use sparingly)
NODE_OPTIONS='--inspect' pnpm run start
```

### Browser DevTools Integration
```bash
# Start with inspector
NODE_OPTIONS='--inspect' pnpm run dev

# Open Chrome → chrome://inspect → Click "inspect"
# Debug server-side code in browser DevTools
```

### MCP Debugging
```bash
# Debug MCP server with detailed logging
DEBUG=mcp:* pnpm run mcp:start

# Test MCP connection
pnpm run mcp:test

# Validate MCP configuration
pnpm run mcp:validate
```

### Debug Features Include:
- ✅ **Server Component Debugging** - Debug SSR and server actions
- ✅ **API Route Debugging** - Step through API endpoints
- ✅ **Client Component Debugging** - React component state/props
- ✅ **Three.js Performance Debugging** - Monitor graphics performance
- ✅ **Database Query Debugging** - Trace SQL queries
- ✅ **MCP Protocol Debugging** - Debug AI assistant integration
- ✅ **TypeScript Source Maps** - Debug original TypeScript code
- ✅ **Hot Reload Compatible** - Changes apply without restart

## 📁 Project Structure

```
repomind-ai/
├── 📁 .vscode/                 # VS Code debugging configuration
│   └── 📄 launch.json         # Debug configurations
├── 📁 .next/                   # Next.js build output
├── 📁 backend/                 # Python FastAPI backend
│   ├── 📁 app/
│   │   ├── 📄 main.py         # FastAPI main application
│   │   ├── 📁 routers/        # API route handlers
│   │   ├── 📁 services/       # Business logic services
│   │   └── 📁 models/         # Database models
├── 📁 mcp/                     # MCP Server implementation
│   ├── 📄 server.ts           # MCP server entry point
│   ├── 📁 tools/              # MCP tool implementations
│   ├── 📁 handlers/           # Request handlers
│   └── 📄 types.ts            # MCP type definitions
├── 📁 src/                     # Frontend source code
│   ├── 📁 app/                # Next.js App Router pages
│   │   ├── 📄 page.tsx        # Home page
│   │   ├── 📄 layout.tsx      # Root layout
│   │   └── 📁 api/            # API routes
│   ├── 📁 components/         # React components
│   │   ├── 📁 ui/             # ShadCN UI components
│   │   ├── 📁 three/          # Three.js components
│   │   └── 📁 mcp/            # MCP integration components
│   ├── 📁 lib/                # Utility functions
│   └── 📁 hooks/              # Custom React hooks
├── 📁 public/                  # Static assets
├── 📄 package.json            # Dependencies and scripts
├── 📄 next.config.js          # Next.js configuration
├── 📄 tailwind.config.ts      # Tailwind CSS configuration
├── 📄 tsconfig.json           # TypeScript configuration
├── 📄 drizzle.config.ts       # Database configuration
├── 📄 mcp.config.json         # MCP server configuration
└── 📄 docker-compose.yml      # Docker services
```

## 🛠 Development Commands

### Frontend Development
```bash
# Development with Turbo
pnpm run dev

# Development with debugging
pnpm run dev:debug

# Type checking
pnpm run typecheck

# Linting and formatting
pnpm run lint
pnpm run lint:fix
pnpm run format:write
pnpm run format:check

# Build and preview
pnpm run build
pnpm run preview
```

### MCP Development
```bash
# Start MCP server
pnpm run mcp:start

# Start MCP server with debugging
pnpm run mcp:debug

# Test MCP functionality
pnpm run mcp:test

# Validate MCP configuration
pnpm run mcp:validate

# Build MCP server
pnpm run mcp:build
```

### Database Operations
```bash
# Generate migrations
pnpm run db:generate

# Apply migrations
pnpm run db:migrate

# Push schema changes
pnpm run db:push

# Open database studio
pnpm run db:studio
```

### Backend Development
```bash
# Start backend with Docker
docker-compose up --build -d

# View logs
docker-compose logs -f

# Stop backend
docker-compose down
```

## 🔐 Security & Authentication

### GitHub Integration
RepoMind AI supports both public and private repository analysis:

#### Public Repositories
- No authentication required
- Direct URL analysis (github.com → gitdiagram.com)
- Full feature access

#### Private Repositories
1. **Generate GitHub Personal Access Token:**
   - Go to GitHub Settings → Developer settings → Personal access tokens
   - Create token with `repo` scope
   - Copy token securely

2. **Configure in Application:**
   - Click "Private Repos" in header
   - Enter your GitHub token
   - Token stored locally in browser only

3. **MCP Integration:**
   ```bash
   # Set environment variable
   export GITHUB_TOKEN="your_token_here"
   
   # Or add to .env file
   echo "GITHUB_TOKEN=your_token_here" >> .env
   ```

### DeepSeek AI Integration
1. **Get API Key:**
   - Visit [DeepSeek Platform](https://platform.deepseek.com/)
   - Create account and generate API key
   - More cost-effective than OpenAI

2. **Configure:**
   ```bash
   export DEEPSEEK_API_KEY="your_key_here"
   ```

## 🤔 About

I created this because I wanted to contribute to open-source projects but quickly realized their codebases are too massive for me to dig through manually, so this helps me get started - but it's definitely got many more use cases!

Given any public (or private!) GitHub repository it generates diagrams in Mermaid.js with DeepSeek AI! (Previously OpenAI o4-mini)

I extract information from the file tree and README for details and interactivity (you can click components to be taken to relevant files and directories)

Most of what you might call the "processing" of this app is done with prompt engineering - see `/backend/app/prompts.py`. This basically extracts and pipelines data and analysis for a larger action workflow, ending in the diagram code.

## 🔒 How to diagram private repositories

You can simply click on "Private Repos" in the header and follow the instructions by providing a GitHub personal access token with the `repo` scope.

You can also self-host this app locally (backend separated as well!) with the steps above.

## 🚀 Deployment

### Vercel (Recommended)
```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel

# Set environment variables in Vercel dashboard
```

### Docker
```bash
# Build and run with Docker Compose
docker-compose up --build

# Production build
docker-compose -f docker-compose.prod.yml up --build
```

### MCP Server Deployment
```bash
# Build for production
pnpm run mcp:build

# Deploy to npm (for distribution)
npm publish

# Docker deployment
docker build -t repomind-mcp -f Dockerfile.mcp .
docker run -p 3001:3001 repomind-mcp
```

## 🆘 Troubleshooting

### Common Issues

**MCP Connection Issues**
```bash
# Check MCP server status
curl http://localhost:3001/health

# Restart MCP server
pnpm run mcp:restart

# Debug MCP protocol
DEBUG=mcp:* pnpm run mcp:start
```

**Debugging Not Working**
- Verify `.vscode/launch.json` exists
- Check TypeScript compilation: `pnpm run typecheck`
- Restart VS Code
- Use `pnpm run dev:debug` instead

**Build Errors**
```bash
# Clear cache and reinstall
rm -rf .next node_modules
pnpm install
pnpm run build
```

**Database Connection**
```bash
# Check database status
./start-database.sh
pnpm run db:studio
```

**Port Conflicts**
```bash
# Kill processes on ports
lsof -ti:6002 | xargs kill -9  # Frontend
lsof -ti:8000 | xargs kill -9  # Backend
lsof -ti:3001 | xargs kill -9  # MCP Server
```

**Backend Issues**
```bash
# Check backend logs
docker-compose logs -f

# Restart backend
docker-compose down && docker-compose up --build -d
```

**GitHub API Rate Limits**
- Ensure GitHub token is properly configured
- Check token permissions (needs `repo` scope for private repos)
- Monitor rate limit headers in API responses

## 📊 Performance & Monitoring

### Enhanced Performance Features
- ⚡ **Turbo Mode**: Faster builds and hot reload
- 🗜 **Automatic Code Splitting**: Optimized bundle sizes
- 🖼 **Image Optimization**: Next.js automatic optimization
- 📦 **Bundle Analysis**: `pnpm run analyze` (add to scripts)
- 🔄 **Progressive Enhancement**: Works without JavaScript
- 🤖 **MCP Optimization**: Efficient AI assistant communication

### Debugging Performance
- **Three.js Monitoring**: Frame rate and memory usage tracking
- **API Response Times**: Built-in performance logging
- **Database Query Performance**: Drizzle ORM query analysis
- **MCP Protocol Performance**: Message throughput and latency
- **Web Vitals**: Core performance metrics tracking

## 🔮 Advanced Features

### AI-Powered Development
With MCP integration, RepoMind AI enables:

- **Intelligent Code Completion**: Context-aware suggestions
- **Automated Refactoring**: AI-driven code improvements
- **Pattern Recognition**: Identify and replicate code patterns
- **Architecture Analysis**: Deep structural insights
- **Performance Optimization**: AI-suggested improvements
- **Security Auditing**: Automated vulnerability detection

### Real-time Collaboration
- **Live Repository Monitoring**: Track changes as they happen
- **Team Insights**: Collaborative development analytics
- **Smart Notifications**: AI-filtered important updates
- **Cross-repository Analysis**: Multi-project insights

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Workflow
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes with proper debugging
4. Test MCP integration: `pnpm run mcp:test`
5. Run tests: `pnpm run test`
6. Commit with conventional commits: `git commit -m "feat: add amazing feature"`
7. Push: `git push origin feature/amazing-feature`
8. Open a Pull Request

### MCP Development Guidelines
- Follow MCP protocol specifications
- Test with multiple AI assistants
- Document new tools and handlers
- Ensure backwards compatibility
- Add comprehensive error handling

## Acknowledgements

- Shoutout to [Romain Courtois](https://github.com/cyclotruc)'s [Gitingest](https://gitingest.com/) for inspiration and styling
- **Next.js Team** - Amazing React framework evolution
- **Three.js Community** - 3D graphics excellence
- **ShadCN** - Beautiful UI components
- **Vercel** - Outstanding deployment platform
- **Anthropic** - MCP protocol and Claude integration
- **DeepSeek** - Powerful and cost-effective AI analysis

## 📈 Rate Limits

I am currently hosting it for free with no rate limits though this is somewhat likely to change in the future.

**MCP Usage Limits:**
- GitHub API: 5,000 requests/hour (authenticated)
- DeepSeek API: Based on your plan
- Repository Analysis: No artificial limits

## 🤔 Future Steps

- ✅ Enhanced debugging infrastructure (completed)
- ✅ Modern development tooling (completed)
- ✅ MCP integration (completed)
- 🔄 Real-time collaboration features
- 📱 Mobile app development
- 🔌 VS Code extension
- 🌐 Multi-language support
- 🤖 Advanced AI features
- 📊 Analytics dashboard
- 🔗 Enhanced Git integration
- 🎯 Enterprise features
- 🔮 Multi-LLM support (GPT-4, Claude, Gemini)
- 🚀 Workflow automation
- 📡 Webhook integrations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**⭐ Star this repo if you find it helpful! ⭐**

*Built with ❤️ by developers, for developers*

[![Built with Next.js](https://img.shields.io/badge/Built%20with-Next.js-black)](https://nextjs.org/)
[![Powered by TypeScript](https://img.shields.io/badge/Powered%20by-TypeScript-blue)](https://www.typescriptlang.org/)
[![Enhanced with Three.js](https://img.shields.io/badge/Enhanced%20with-Three.js-red)](https://threejs.org/)
[![MCP Enabled](https://img.shields.io/badge/MCP-Enabled-purple)](https://modelcontextprotocol.io/)
[![Claude Ready](https://img.shields.io/badge/Claude-Ready-orange)](https://claude.ai/)

</div>