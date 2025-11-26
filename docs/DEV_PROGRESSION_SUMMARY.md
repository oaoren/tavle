# Development Progression Summary

## Recommended Tech Stack

### Phase 1: Static Site (GitHub Pages)
- **Python** - Build script language
- **Jinja2** - HTML templating
- **PyYAML** - YAML parsing
- **Vanilla JS** - Minimal interactivity (no React)
- **Output:** Static HTML/CSS/JS

### Phase 2+: Dynamic Site (FastAPI)
- **FastAPI** - Backend API
- **Jinja2** - Server-side rendering
- **HTMX** - Minimal JS interactions (alternative to React)
- **PyYAML** - Still using YAML files (or migrate to DB later)

## Why This Approach?

✅ **Python-first** - Your main language for everything
✅ **No React needed** - Jinja2 + HTMX covers all frontend needs
✅ **Minimal JavaScript** - Only where absolutely necessary
✅ **Free hosting** - Phase 1 on GitHub Pages, Phase 2 on free tier (Railway, Render, etc.)
✅ **Simple architecture** - YAML files → Python processing → HTML output

## Phase 1 Task Flow

1. **Setup** (Tasks 1.1-1.4)
   - Project structure
   - Python environment
   - GitHub Pages config

2. **Data** (Tasks 1.5-1.8)
   - Design YAML schema
   - Create dummy posts
   - Build Python YAML loader

3. **Templates** (Tasks 1.9-1.14)
   - Jinja2 base template
   - Post card template
   - Listing page template
   - Screen display template
   - CSS styling

4. **Build System** (Tasks 1.15-1.17)
   - Python build script
   - Minimal JS for interactivity
   - Test locally

5. **Deploy** (Tasks 1.18-1.21)
   - GitHub Actions workflow
   - Test deployment
   - Test on devices

6. **Documentation** (Tasks 1.22-1.24)
   - YAML schema docs
   - Deployment guide
   - Dev setup instructions

## Quick Start Order

Suggested priority order for Phase 1:

1. **High Priority:**
   - Task 1.2: Python environment setup
   - Task 1.5: YAML schema design
   - Task 1.7: Create dummy posts
   - Task 1.8: YAML loader
   - Task 1.9: Base template
   - Task 1.15: Build script

2. **Medium Priority:**
   - Task 1.11: Post card template
   - Task 1.12: Listing template
   - Task 1.10: CSS styling
   - Task 1.16: Minimal JS

3. **Lower Priority:**
   - Task 1.14: Screen display template
   - Task 1.18: GitHub Actions
   - Documentation tasks

## Next Steps

1. Fill in `priority []` fields in `PROGRESSION.md`
2. Start with high-priority tasks
3. Build iteratively: data → templates → build → deploy
4. Test frequently on target devices

