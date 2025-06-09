# Development Guide for RepoMind AI

This guide provides detailed development instructions for working with RepoMind AI.

## 🛠 Development Environment Setup

### System Requirements
- **macOS/Linux/Windows** with Docker support
- **Node.js 18.17+** (recommended: use nvm)
- **pnpm 9.13.0+** package manager
- **Python 3.13+** for backend
- **PostgreSQL 14+** (via Docker)
- **VS Code** with debugging extensions

### Initial Setup

1. **Clone and Navigate**
   ```bash
   git clone https://github.com/itrimble/repomind-ai.git
   cd repomind-ai
   ```

2. **Install Frontend Dependencies**
   ```bash
   pnpm install
   ```

3. **Environment Configuration**
   ```bash
   cp .env.example .env
   ```

   Edit `.env` with your configuration:
   ```env
   # Required for AI analysis
   DEEPSEEK_API_KEY="your_deepseek_api_key"
   
   # Required for private repos
   GITHUB_TOKEN="your_github_personal_access_token"
   
   # Database (auto-configured by start-database.sh)
   DATABASE_URL="postgresql://postgres:password@localhost:5432/repomind"
   
   # Optional: Analytics
   POSTHOG_KEY="your_posthog_key"
   POSTHOG_HOST="https://us.i.posthog.com"
   
   # Development
   NODE_ENV="development"
   NEXT_PUBLIC_APP_URL="http://localhost:6002"
   ```

## 🗄 Database Setup

### Automatic Setup (Recommended)
```bash
# Make script executable and run
chmod +x start-database.sh
./start-database.sh

# When prompted for password generation, type: yes
# Note the generated password for your .env file
```

### Manual Database Setup
```bash
# Start PostgreSQL with Docker
docker run -d \
  --name repomind-postgres \
  -e POSTGRES_DB=repomind \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=your_password \
  -p 5432:5432 \
  postgres:14

# Apply database schema
pnpm run db:push

# Optional: View database
pnpm run db:studio
```

## 🐍 Backend Development

### Quick Start with Docker (Recommended)
```bash
# Start all backend services
docker-compose up --build -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Manual Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start FastAPI server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 🎯 Frontend Development

### Development Server
```bash
# Standard development
pnpm run dev

# Development with debugging enabled
pnpm run dev:debug

# Production build test
pnpm run build && pnpm run start
```

### Development Scripts
```bash
# Type checking
pnpm run typecheck

# Linting
pnpm run lint           # Check for issues
pnpm run lint:fix       # Auto-fix issues

# Code formatting
pnpm run format:check   # Check formatting
pnpm run format:write   # Apply formatting

# Database operations
pnpm run db:generate    # Generate migration
pnpm run db:migrate     # Apply migration
pnpm run db:push        # Push schema changes
pnpm run db:studio      # Open database UI
```

## 🔧 VS Code Debugging Setup

### Automatic Setup
The `.vscode/launch.json` file is already configured with these options:

1. **Next.js: debug server-side** - Debug API routes and server components
2. **Next.js: debug client-side** - Debug React components in Chrome
3. **Next.js: debug client-side (Firefox)** - Debug React components in Firefox  
4. **Next.js: debug full stack** - Combined server + client debugging

### Using the Debugger

1. **Open VS Code**
   ```bash
   code .
   ```

2. **Start Debugging Session**
   - Press `⇧+⌘+D` (macOS) or `Ctrl+Shift+D` (Windows/Linux)
   - Select your debug configuration
   - Press `F5` or click the play button

3. **Set Breakpoints**
   - Click in the gutter next to line numbers
   - Or press `F9` on the desired line
   - Breakpoints work in `.ts`, `.tsx`, and `.js` files

### Debug Configurations Explained

#### Server-Side Debugging
```json
{
  "name": "Next.js: debug server-side",
  "type": "node-terminal",
  "request": "launch", 
  "command": "pnpm run dev"
}
```
- Debugs API routes, server components, middleware
- Breakpoints in `/src/app/api/*` routes
- Server-side React component rendering

#### Full Stack Debugging  
```json
{
  "name": "Next.js: debug full stack",
  "type": "node",
  "request": "launch",
  "program": "${workspaceFolder}/node_modules/next/dist/bin/next",
  "runtimeArgs": ["--inspect"],
  "serverReadyAction": {
    "action": "debugWithChrome",
    "pattern": "- Local:.+(https?://.+)"
  }
}
```
- Debugs both server and client code
- Automatically opens Chrome with debugger attached
- Best for comprehensive debugging sessions

## 🧪 Testing and Quality Assurance

### Type Checking
```bash
# Full TypeScript check
pnpm run typecheck

# Watch mode (continuous checking)
npx tsc --noEmit --watch
```

### Code Quality
```bash
# Run all quality checks
pnpm run check

# Individual checks
pnpm run lint           # ESLint
pnpm run format:check   # Prettier
pnpm run typecheck      # TypeScript
```

### Performance Testing
```bash
# Build analysis
pnpm run build

# Bundle analyzer (add to package.json if needed)
ANALYZE=true pnpm run build
```

## 🔍 Debugging Common Issues

### Frontend Issues

**Hot Reload Not Working**
```bash
# Clear Next.js cache
rm -rf .next

# Restart dev server
pnpm run dev:debug
```

**TypeScript Errors**
```bash
# Check for errors
pnpm run typecheck

# Common fix: restart TypeScript server in VS Code
# Command Palette > TypeScript: Restart TS Server
```

**Breakpoints Not Hitting**
1. Ensure VS Code is using the workspace TypeScript version
2. Check that source maps are enabled in `next.config.js`
3. Restart debugging session (`Shift+F5` then `F5`)

### Backend Issues

**Docker Container Issues**
```bash
# View container logs
docker-compose logs backend

# Restart containers
docker-compose down && docker-compose up --build -d

# Shell into container
docker-compose exec backend bash
```

**Database Connection Issues**
```bash
# Check database container
docker ps | grep postgres

# Test connection
docker-compose exec postgres psql -U postgres -d repomind -c "SELECT 1;"

# Restart database
./start-database.sh
```

**API Errors**
```bash
# Check API health
curl http://localhost:8000/health

# View detailed logs
docker-compose logs -f backend
```

### Environment Issues

**Port Conflicts**
```bash
# Find processes using ports
lsof -ti:6002  # Frontend
lsof -ti:8000  # Backend
lsof -ti:5432  # Database

# Kill processes
lsof -ti:6002 | xargs kill -9
```

**Environment Variables**
```bash
# Check if variables are loaded
node -e "console.log(process.env.DEEPSEEK_API_KEY ? 'API key loaded' : 'API key missing')"

# Verify .env file exists and has correct format
cat .env | grep -v "^#" | grep "="
```

## 📈 Performance Optimization

### Frontend Performance
- Monitor bundle size with webpack-bundle-analyzer
- Check Core Web Vitals in browser DevTools
- Profile Three.js rendering performance
- Test on slower devices and networks

### Backend Performance
- Monitor API response times
- Profile database queries
- Check memory usage with container stats
- Load test with multiple concurrent requests

### Database Performance
```sql
-- Check slow queries (when implemented)
SELECT query, mean_exec_time, calls 
FROM pg_stat_statements 
ORDER BY mean_exec_time DESC 
LIMIT 10;

-- Check database size
SELECT pg_size_pretty(pg_database_size('repomind'));
```

## 🚀 Deployment Preparation

### Pre-deployment Checklist
- [ ] All tests pass
- [ ] TypeScript compilation successful
- [ ] No ESLint errors
- [ ] Environment variables configured
- [ ] Database migrations applied
- [ ] Performance testing completed
- [ ] Security audit passed

### Production Build Testing
```bash
# Build and test production
pnpm run build
pnpm run start

# Test production API
NODE_ENV=production uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 🔧 Development Tools

### Recommended VS Code Extensions
- TypeScript and JavaScript Language Features
- ESLint
- Prettier
- Tailwind CSS IntelliSense
- Auto Rename Tag
- Bracket Pair Colorizer
- GitLens
- Thunder Client (API testing)

### Browser DevTools Setup
- Install React Developer Tools
- Install Redux DevTools (if using Redux)
- Enable Three.js performance monitoring
- Configure network throttling for testing

### Terminal Setup
```bash
# Useful aliases (add to ~/.zshrc or ~/.bashrc)
alias repomind-dev="cd /path/to/repomind-ai && pnpm run dev:debug"
alias repomind-logs="cd /path/to/repomind-ai && docker-compose logs -f"
alias repomind-db="cd /path/to/repomind-ai && pnpm run db:studio"
```

## 📚 Additional Resources

### Documentation
- [Next.js Documentation](https://nextjs.org/docs)
- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [Three.js Documentation](https://threejs.org/docs/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [ShadCN UI Documentation](https://ui.shadcn.com/)

### Learning Resources
- [Next.js Learn Course](https://nextjs.org/learn)
- [TypeScript Deep Dive](https://basarat.gitbook.io/typescript/)
- [Three.js Journey](https://threejs-journey.com/)
- [React Debugging Guide](https://react.dev/learn/debugging)

This development guide should provide everything you need to contribute effectively to RepoMind AI. Happy coding! 🚀