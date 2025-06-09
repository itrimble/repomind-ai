# Screenshots Directory

This directory contains screenshots of the RepoMind AI application for documentation purposes.

## Screenshot Files

- `hero-section.png` - Main hero section showing the primary value proposition
- `demo-section.png` - Interactive demo section with repository examples
- `features-section.png` - Features and capabilities overview
- `pricing-section.png` - Transparent pricing information
- `testimonials-section.png` - Customer testimonials and use cases
- `dashboard.png` - Main application dashboard
- `analysis-results.png` - Repository analysis results view
- `diagram-viewer.png` - Interactive diagram visualization
- `debugging-interface.png` - VS Code debugging interface

## Capturing Screenshots

To capture new screenshots:

1. Start the development server:
   ```bash
   pnpm run dev
   ```

2. Navigate to http://localhost:6002

3. Use browser tools or the capture MCP to take screenshots:
   ```bash
   # Using the capture tool
   capture --region full --format png
   ```

4. Save screenshots to this directory with descriptive names

## Usage in Documentation

Screenshots are referenced in documentation using:

```rst
.. image:: screenshots/hero-section.png
   :alt: RepoMind AI Hero Section
   :width: 800px
```

## Guidelines

- Use PNG format for better quality
- Optimize file sizes (keep under 1MB each)
- Use descriptive filenames
- Include alt text for accessibility
- Show actual application content when possible
- Use consistent browser/viewport sizes

## Updating Screenshots

Screenshots should be updated when:
- UI/UX changes significantly
- New features are added
- Color scheme or branding changes
- Documentation requires new visual examples