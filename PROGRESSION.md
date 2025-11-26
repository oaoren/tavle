# Tavla Development Progression

This document tracks development tasks organized by phase. Each task includes a `priority []` field for manual prioritization.

## Technology Approach

**Phase 1:** Python-based static site generation
- Python script processes YAML files
- Jinja2 templates generate HTML
- Minimal vanilla JavaScript (no React)
- Output: Static HTML/CSS/JS for GitHub Pages

**Future Phases:** FastAPI + Python frontend
- FastAPI backend API
- Jinja2 server-side rendering
- HTMX for minimal JavaScript interactions
- Alternative: Reflex/NiceGUI if Python-native frontend needed

## Phase 1: Minimal Webpage Deployment

**Goal:** Deploy a minimal webpage on GitHub Pages displaying dummy posts from YAML files.

### Setup & Infrastructure

- [ ] **Task 1.1:** Initialize project structure (folders: `src/`, `data/`, `public/`, `docs/`)
  - Priority: []
  - Notes: Create basic folder structure for organizing code and data

- [ ] **Task 1.2:** Set up Python build environment
  - Priority: []
  - Notes: Create `requirements.txt` with PyYAML, Jinja2. Set up virtual environment

- [ ] **Task 1.3:** Configure GitHub Pages deployment workflow
  - Priority: []
  - Notes: Set up GitHub Actions or configure Pages settings

- [ ] **Task 1.4:** Create `.gitignore` file
  - Priority: []
  - Notes: Exclude __pycache__, venv/, build artifacts, etc.

### Data Structure 

- [ ] **Task 1.5:** Design YAML schema for posts
  - Priority: []
  - Notes: Define structure for events, general info, and ads

- [ ] **Task 1.6:** Create folder structure for organizing posts (e.g., `data/events/`, `data/info/`, `data/ads/`)
  - Priority: []
  - Notes: Organize by post type

- [ ] **Task 1.7:** Create dummy post YAML files (at least 3-5 examples)
  - Priority: []
  - Notes: Include examples of each post type

- [ ] **Task 1.8:** Create YAML parser/loader utility (Python)
  - Priority: []
  - Notes: Python function to read and parse YAML files from data/ folders. Returns structured data for templates

### Template & Frontend Development

- [ ] **Task 1.9:** Create Jinja2 base template
  - Priority: []
  - Notes: Base HTML template with semantic structure, proper meta tags, and template blocks

- [ ] **Task 1.10:** Design and implement basic CSS styling
  - Priority: []
  - Notes: Responsive design for mobile, tablet, desktop, and screen display. Store in `public/css/`

- [ ] **Task 1.11:** Create Jinja2 post card template
  - Priority: []
  - Notes: Reusable Jinja2 template macro/partial to render individual posts

- [ ] **Task 1.12:** Create Jinja2 post listing template
  - Priority: []
  - Notes: Template to display all posts, possibly with filtering by type (client-side JS if needed)

- [ ] **Task 1.13:** Add basic responsive design
  - Priority: []
  - Notes: Ensure mobile, tablet, and desktop views work well with CSS media queries

- [ ] **Task 1.14:** Create dedicated screen display template/page
  - Priority: []
  - Notes: Separate Jinja2 template optimized for physical screen in shop (large text, auto-refresh via JS)

### Build System & Integration

- [ ] **Task 1.15:** Create Python build script
  - Priority: []
  - Notes: Script that loads YAML files, renders Jinja2 templates, outputs static HTML to `dist/` or `docs/` folder

- [ ] **Task 1.16:** Add minimal JavaScript for interactivity (if needed)
  - Priority: []
  - Notes: Vanilla JS only - filtering, auto-refresh for screen display, etc. No React.

- [ ] **Task 1.17:** Test build script locally
  - Priority: []
  - Notes: Run build script, verify generated HTML, test in browser

- [ ] **Task 1.18:** Configure GitHub Pages deployment
  - Priority: []
  - Notes: Set up GitHub Actions workflow to run build script and deploy, or configure Pages to serve from `docs/` folder

- [ ] **Task 1.19:** Test GitHub Pages deployment
  - Priority: []
  - Notes: Deploy and verify site works on GitHub Pages

- [ ] **Task 1.20:** Test responsive design on multiple devices
  - Priority: []
  - Notes: Mobile, tablet, desktop, and screen display

- [ ] **Task 1.21:** Test screen display view on target device
  - Priority: []
  - Notes: Verify physical screen display works correctly

### Documentation

- [ ] **Task 1.22:** Document YAML post format/schema
  - Priority: []
  - Notes: Create documentation for adding new posts (update `docs/YAML_SCHEMA.md`)

- [ ] **Task 1.23:** Create deployment guide
  - Priority: []
  - Notes: Instructions for deploying updates (build script → GitHub Pages)

- [ ] **Task 1.24:** Add development setup instructions to README
  - Priority: []
  - Notes: How to set up Python venv, install dependencies, run build script locally

---

## Phase 2: Social Media Integration (Future)

**Goal:** Add optional auto-posting to Instagram and Facebook.

### Tasks will be added here as Phase 1 completes...

---

## Phase 3: Additional Features (Future)

**Goal:** Expand social media integration and add webapp capabilities.

### Tasks will be added here as Phase 2 completes...

