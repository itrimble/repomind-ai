# 🧠 RepoMind AI (GitDiagram)

[![Image](./docs/readme_img.png "GitDiagram Front Page")](https://gitdiagram.com/)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
[![Kofi](https://img.shields.io/badge/Kofi-F16061.svg?logo=ko-fi&logoColor=white)](https://ko-fi.com/ahmedkhaleel2004)
![Next.js](https://img.shields.io/badge/Next.js-15.3.3-black) ![TypeScript](https://img.shields.io/badge/TypeScript-5.5.3-blue) ![Three.js](https://img.shields.io/badge/Three.js-Interactive%20Graphics-red)

Turn any GitHub repository into an interactive diagram for visualization in seconds. Now with enhanced debugging capabilities and modern development tools.

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

# Check backend logs
docker-compose logs -f
```

### 5. Access Application
- **Frontend**: http://localhost:6002
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
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
4. Press `F5` to start debugging
5. Set breakpoints and debug in real-time!

### Debug Scripts
```bash
# Server-side debugging with Node inspector
pnpm run dev:debug

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

### Debug Features Include:
- ✅ **Server Component Debugging** - Debug SSR and server actions
- ✅ **API Route Debugging** - Step through API endpoints
- ✅ **Client Component Debugging** - React component state/props
- ✅ **Three.js Performance Debugging** - Monitor graphics performance
- ✅ **Database Query Debugging** - Trace SQL queries
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
├── 📁 src/                     # Frontend source code
│   ├── 📁 app/                # Next.js App Router pages
│   │   ├── 📄 page.tsx        # Home page
│   │   ├── 📄 layout.tsx      # Root layout
│   │   └── 📁 api/            # API routes
│   ├── 📁 components/         # React components
│   │   ├── 📁 ui/             # ShadCN UI components
│   │   └── 📁 three/          # Three.js components
│   ├── 📁 lib/                # Utility functions
│   └── 📁 hooks/              # Custom React hooks
├── 📁 public/                  # Static assets
├── 📄 package.json            # Dependencies and scripts
├── 📄 next.config.js          # Next.js configuration
├── 📄 tailwind.config.ts      # Tailwind CSS configuration
├── 📄 tsconfig.json           # TypeScript configuration
├── 📄 drizzle.config.ts       # Database configuration
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

## 🆘 Troubleshooting

### Common Issues

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
lsof -ti:6002 | xargs kill -9
lsof -ti:8000 | xargs kill -9
```

**Backend Issues**
```bash
# Check backend logs
docker-compose logs -f

# Restart backend
docker-compose down && docker-compose up --build -d
```

## 📊 Performance & Monitoring

### Enhanced Performance Features
- ⚡ **Turbo Mode**: Faster builds and hot reload
- 🗜 **Automatic Code Splitting**: Optimized bundle sizes
- 🖼 **Image Optimization**: Next.js automatic optimization
- 📦 **Bundle Analysis**: `pnpm run analyze` (add to scripts)
- 🔄 **Progressive Enhancement**: Works without JavaScript

### Debugging Performance
- **Three.js Monitoring**: Frame rate and memory usage tracking
- **API Response Times**: Built-in performance logging
- **Database Query Performance**: Drizzle ORM query analysis
- **Web Vitals**: Core performance metrics tracking

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Workflow
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes with proper debugging
4. Run tests: `pnpm run test`
5. Commit with conventional commits: `git commit -m "feat: add amazing feature"`
6. Push: `git push origin feature/amazing-feature`
7. Open a Pull Request

## Acknowledgements

- Shoutout to [Romain Courtois](https://github.com/cyclotruc)'s [Gitingest](https://gitingest.com/) for inspiration and styling
- **Next.js Team** - Amazing React framework evolution
- **Three.js Community** - 3D graphics excellence
- **ShadCN** - Beautiful UI components
- **Vercel** - Outstanding deployment platform

## 📈 Rate Limits

I am currently hosting it for free with no rate limits though this is somewhat likely to change in the future.

## 🤔 Future Steps

- ✅ Enhanced debugging infrastructure (completed)
- ✅ Modern development tooling (completed)
- 🔄 Real-time collaboration features
- 📱 Mobile app development
- 🔌 VS Code extension
- 🌐 Multi-language support
- 🤖 Advanced AI features
- 📊 Analytics dashboard
- 🔗 Enhanced Git integration
- 🎯 Enterprise features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**⭐ Star this repo if you find it helpful! ⭐**

*Built with ❤️ by developers, for developers*

[![Built with Next.js](https://img.shields.io/badge/Built%20with-Next.js-black)](https://nextjs.org/)
[![Powered by TypeScript](https://img.shields.io/badge/Powered%20by-TypeScript-blue)](https://www.typescriptlang.org/)
[![Enhanced with Three.js](https://img.shields.io/badge/Enhanced%20with-Three.js-red)](https://threejs.org/)

</div>