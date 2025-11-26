# Python Frontend Approach

## Recommendation: Python-Driven Frontend (No React Needed)

Given that Python is your main language and you want minimal React, here's the recommended approach:

## Phase 1: Static Site Generation (Python)

**Approach:** Python script + Jinja2 templates → Static HTML

**Why this works:**
- ✅ Pure Python (your main language)
- ✅ No React needed
- ✅ Jinja2 is Python-native, powerful templating
- ✅ Generates static HTML for GitHub Pages (free hosting)
- ✅ Minimal JavaScript (only for interactivity like filtering, auto-refresh)

**Workflow:**
1. Python script reads YAML files from `data/` folders
2. Jinja2 templates render posts into HTML
3. Output static HTML/CSS/JS to `docs/` folder
4. GitHub Pages serves the static files

## Future Phases: FastAPI + Python Frontend

### Option 1: FastAPI + Jinja2 + HTMX (Recommended)

**Stack:**
- FastAPI backend API
- Jinja2 server-side rendering
- HTMX for dynamic interactions (minimal JS, no React)

**Why HTMX:**
- ✅ Minimal JavaScript (just HTML attributes)
- ✅ Server-side rendering (Python logic)
- ✅ No React complexity
- ✅ Works seamlessly with FastAPI

**Example:**
```html
<!-- HTMX replaces React components -->
<button hx-get="/api/posts" hx-target="#posts">
  Refresh Posts
</button>
```

### Option 2: Python Frontend Frameworks (If Needed)

If you need more interactivity later, consider:

**Reflex** (Python React alternative)
- Write React-like components in Python
- Compiles to React under the hood
- Good if you want component-based architecture in Python

**NiceGUI**
- Python UI framework
- Good for admin panels, dashboards
- Might be overkill for a billboard

**Streamlit**
- Great for data apps
- Probably too heavy for this use case

## Recommendation Summary

**Phase 1:** Python + Jinja2 → Static HTML (no React)
**Phase 2+:** FastAPI + Jinja2 + HTMX (minimal JS, no React)

This keeps you in Python for 95% of the code, with minimal JavaScript only where needed for interactivity.

