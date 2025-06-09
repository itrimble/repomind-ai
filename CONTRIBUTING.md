# Contributing to RepoMind AI

Thank you for your interest in contributing to RepoMind AI! This guide will help you get started with contributing to this project.

## 🚀 Quick Start for Contributors

### Prerequisites
- Node.js 18.17+
- pnpm 9.13.0+
- Python 3.13+
- Git
- VS Code (recommended for debugging)

### Setup Development Environment

1. **Fork and Clone**
   ```bash
   # Fork the repository on GitHub first
   git clone https://github.com/YOUR_USERNAME/repomind-ai.git
   cd repomind-ai
   ```

2. **Install Dependencies**
   ```bash
   pnpm install
   ```

3. **Environment Setup**
   ```bash
   cp .env.example .env
   # Add your API keys to .env
   ```

4. **Start Development**
   ```bash
   # Terminal 1: Frontend
   pnpm run dev:debug

   # Terminal 2: Backend
   docker-compose up --build -d
   ```

## 🛠 Development Workflow

### Branch Strategy
- `main` - Production-ready code
- `develop` - Integration branch
- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `hotfix/*` - Critical fixes

### Making Changes

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Use Debugging Tools**
   - Open VS Code: `code .`
   - Press `⇧+⌘+D` for debug panel
   - Select "Next.js: debug full stack"
   - Set breakpoints and debug your changes

3. **Code Standards**
   - Follow TypeScript strict mode
   - Use ESLint and Prettier configurations
   - Write meaningful commit messages
   - Add tests for new features

4. **Testing Your Changes**
   ```bash
   # Type checking
   pnpm run typecheck
   
   # Linting
   pnpm run lint
   
   # Format code
   pnpm run format:write
   
   # Build test
   pnpm run build
   ```

5. **Commit and Push**
   ```bash
   git add .
   git commit -m "feat: add new feature description"
   git push origin feature/your-feature-name
   ```

## 📝 Code Style Guidelines

### TypeScript/JavaScript
- Use TypeScript strict mode
- Prefer `interface` over `type` for object shapes
- Use meaningful variable and function names
- Add JSDoc comments for complex functions

```typescript
// Good
interface RepositoryAnalysis {
  structure: FileNode[];
  insights: AIInsight[];
  metrics: PerformanceMetrics;
}

// Better with JSDoc
/**
 * Analyzes repository structure and generates AI insights
 * @param repoUrl - GitHub repository URL
 * @param options - Analysis configuration options
 * @returns Promise with complete analysis results
 */
async function analyzeRepository(
  repoUrl: string, 
  options: AnalysisOptions
): Promise<RepositoryAnalysis> {
  // Implementation
}
```

### React Components
- Use functional components with hooks
- Follow ShadCN UI patterns
- Implement proper error boundaries
- Use TypeScript for props

```tsx
// Component example
interface DiagramViewerProps {
  data: DiagramData;
  onNodeClick?: (nodeId: string) => void;
  className?: string;
}

export function DiagramViewer({ 
  data, 
  onNodeClick, 
  className 
}: DiagramViewerProps) {
  // Use debugging-friendly patterns
  useEffect(() => {
    console.log('DiagramViewer mounted with data:', data);
  }, [data]);

  return (
    <div className={cn("diagram-container", className)}>
      {/* Component content */}
    </div>
  );
}
```

### Python Backend
- Follow PEP 8 style guide
- Use type hints
- Add docstrings for functions
- Use async/await for I/O operations

```python
# Good Python example
from typing import List, Optional
from pydantic import BaseModel

class RepositoryRequest(BaseModel):
    url: str
    include_private: bool = False
    analysis_depth: Optional[str] = "full"

async def analyze_repository(
    request: RepositoryRequest
) -> Dict[str, Any]:
    """
    Analyze repository structure and generate insights.
    
    Args:
        request: Repository analysis request parameters
        
    Returns:
        Dictionary containing analysis results
    """
    # Implementation
```

## 🐛 Debugging Contributions

### Using the Debug Setup
When working on contributions, make full use of the debugging infrastructure:

1. **Server-Side Debugging**
   ```bash
   # Start with debugging
   pnpm run dev:debug
   
   # Set breakpoints in:
   # - API routes (src/app/api/*)
   # - Server components
   # - Server actions
   ```

2. **Client-Side Debugging**
   - Use VS Code debugging for React components
   - Browser DevTools for Three.js performance
   - Network tab for API calls

3. **Backend Debugging**
   ```bash
   # View backend logs
   docker-compose logs -f
   
   # Interactive debugging
   docker-compose exec backend python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m uvicorn app.main:app --reload
   ```

### Debugging Best Practices
- Remove `debugger` statements before committing
- Use `console.log` sparingly in production code
- Add meaningful error messages
- Test edge cases and error conditions

## 🧪 Testing Guidelines

### Frontend Testing
```bash
# Unit tests (when implemented)
pnpm run test

# E2E tests (when implemented)
pnpm run test:e2e

# Type checking
pnpm run typecheck
```

### Manual Testing Checklist
- [ ] Repository analysis works with public repos
- [ ] Private repository access functions correctly
- [ ] Diagram generation is accurate
- [ ] Interactive elements work (click navigation)
- [ ] Responsive design on mobile
- [ ] Dark/light theme switching
- [ ] Error handling for invalid repositories

## 📊 Performance Considerations

### Frontend Performance
- Monitor Three.js rendering performance
- Check bundle size with `pnpm run analyze`
- Test on slower devices
- Verify lazy loading works

### Backend Performance
- Monitor API response times
- Check database query performance
- Test with large repositories
- Verify memory usage

## 🚀 Submitting Pull Requests

### PR Requirements
1. **Description**: Clear description of changes
2. **Testing**: All tests pass
3. **Documentation**: Update docs if needed
4. **Breaking Changes**: Note any breaking changes
5. **Screenshots**: For UI changes

### PR Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Local testing completed
- [ ] Debugging setup verified
- [ ] Manual testing completed

## Screenshots (if applicable)
Add screenshots for UI changes

## Additional Notes
Any additional context or notes
```

### Review Process
1. Automated checks must pass
2. Code review by maintainers
3. Testing in staging environment
4. Final approval and merge

## 🔧 Project-Specific Guidelines

### Working with Three.js
- Dispose of geometries and materials properly
- Monitor memory usage
- Test performance on different devices
- Use debugging tools for frame rate analysis

### AI Integration
- Test with different repository types
- Verify API key handling
- Monitor AI service quotas
- Handle API errors gracefully

### Database Changes
- Always create migrations
- Test with existing data
- Document schema changes
- Consider performance impact

## 🆘 Getting Help

### Resources
- **Documentation**: Check the README and Wiki
- **Issues**: Search existing issues first
- **Discussions**: Use GitHub Discussions for questions
- **Discord**: Join our development Discord (if available)

### Common Issues
- **Build Errors**: Clear cache with `rm -rf .next node_modules && pnpm install`
- **Database Issues**: Restart with `./start-database.sh`
- **Docker Issues**: `docker-compose down && docker-compose up --build -d`
- **Debugging Issues**: Verify VS Code extensions and restart

## 🌟 Recognition

Contributors will be:
- Added to the contributors list
- Mentioned in release notes
- Invited to the contributors team (for regular contributors)

## 📄 Code of Conduct

We are committed to providing a welcoming and inspiring community for all. Please read our Code of Conduct before contributing.

### Our Standards
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

## 🎯 Areas for Contribution

### High Priority
- [ ] Enhanced error handling
- [ ] Performance optimizations
- [ ] Mobile experience improvements
- [ ] Accessibility enhancements

### Medium Priority
- [ ] Additional AI model integrations
- [ ] Extended diagram types
- [ ] Real-time collaboration features
- [ ] API rate limiting improvements

### Low Priority
- [ ] Additional themes
- [ ] Internationalization
- [ ] Browser extension
- [ ] Mobile app

Thank you for contributing to RepoMind AI! 🚀