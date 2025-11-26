# Development Setup

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup Instructions

1. **Clone the repository** (if not already done)
   ```bash
   git clone <repository-url>
   cd tavle
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**
   ```bash
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the build script** (once created)
   ```bash
   python src/build.py
   ```

## Project Structure

```
tavle/
├── src/              # Python source code
│   ├── build.py      # Build script (generates static site)
│   └── loader.py     # YAML loader utility
├── templates/        # Jinja2 templates
│   ├── base.html     # Base template
│   └── ...
├── data/             # YAML post files
│   ├── events/
│   ├── info/
│   └── ads/
├── public/           # Static assets (CSS, JS, images)
├── dist/ or docs/    # Generated static HTML (for GitHub Pages)
└── requirements.txt  # Python dependencies
```

## Development Workflow

1. Edit YAML files in `data/` folders
2. Modify Jinja2 templates in `templates/`
3. Update CSS/JS in `public/`
4. Run build script: `python src/build.py`
5. Preview generated HTML locally
6. Commit and push (GitHub Actions will deploy)

## Notes

- Phase 1 uses static site generation (no server needed)
- Future phases will use FastAPI for dynamic content
- All frontend logic is Python + Jinja2 + minimal vanilla JS

