# Tavla (Eiketavla)

A community billboard webapp for sharing information in Eikefjord.

## Overview

**Tavla** (formally known as **Eiketavla**) is a community information platform designed to display:

- **Events** - Local community events and happenings
- **General Information** - Community announcements and news
- **Local Ads** - Advertisements from local businesses

## Deployment Targets

The webapp is designed to work across multiple platforms:

- **Physical Screen Display** - Dedicated page for display in local shop
- **Desktop Browser** - Full-featured web experience
- **Mobile Browser** - Responsive mobile-friendly interface
- **Web App** - Progressive Web App capabilities (later phase)

## Social Media Integration

Posts can optionally be auto-shared to external platforms:

**Initial Phase:**
- Instagram
- Facebook

**Later Phase:**
- Snapchat
- Email
- SMS
- Other platforms

## Technology Stack

**Phase 1 (Static Site):**
- **Python** - Main development language
- **Jinja2** - Template engine for generating HTML
- **PyYAML** - YAML file parsing
- **Vanilla JavaScript** - Minimal JS for interactivity (no React)
- Static site generation via Python build script
- GitHub Pages deployment

**Future Phases:**
- **FastAPI** - Backend API framework
- **Jinja2** - Server-side rendering templates
- **HTMX** - Minimal JavaScript for dynamic interactions (alternative to React)
- Optional: **Reflex** or **NiceGUI** - Python-native frontend frameworks (if needed)

**Architecture:**
- Posts stored as YAML files in organized folder structure
- Phase 1: Python script generates static HTML from YAML
- Later: FastAPI serves dynamic content with Jinja2 templates
- Eliminates need for running database instance (Phase 1)
- Enables free hosting solutions

## Development Status

Currently in **Phase 1** - See `PROGRESSION.md` for detailed task breakdown.

## Project Structure

```
tavle/
├── data/           # YAML files for posts
│   ├── events/     # Event posts
│   ├── info/       # Information posts
│   └── ads/        # Advertisement posts
├── src/            # Python source code
│   ├── loader.py   # YAML post loader
│   └── build.py    # Build script
├── templates/      # Jinja2 HTML templates
├── public/         # Static assets (CSS, JS)
├── docs/           # Generated static HTML (for GitHub Pages)
└── .github/        # GitHub Actions workflows
```

## Quick Start

### Local Development

1. **Set up Python environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Add posts:**
   - Create YAML files in `data/events/`, `data/info/`, or `data/ads/`
   - See `docs/YAML_SCHEMA.md` for format

3. **Build the site:**
   ```bash
   python src/build.py
   ```

4. **Preview locally:**
   ```bash
   cd docs
   python3 -m http.server 8000
   # Open http://localhost:8000
   ```

### Deployment to GitHub Pages

1. **Enable GitHub Pages:**
   - Go to repository Settings → Pages
   - Source: GitHub Actions

2. **Push to main branch:**
   - The GitHub Actions workflow will automatically build and deploy
   - Site will be available at `https://<username>.github.io/tavle/`

3. **Manual deployment:**
   ```bash
   python src/build.py
   git add docs/
   git commit -m "Update site"
   git push
   ```

## Adding Posts

Create YAML files in the appropriate `data/` subdirectory. Example:

```yaml
id: event-003
type: event
title: My Event
content: |
  Event description here.
author: Your Name
date: 2024-01-20
event_date: 2024-02-15
event_time: "19:00"
event_location: Community Center
published: true
tags:
  - community
```

See `docs/YAML_SCHEMA.md` for complete schema documentation.

## License

Apache License 2.0
