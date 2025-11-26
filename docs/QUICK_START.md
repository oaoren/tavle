# Quick Start Guide

## What's Been Set Up

✅ **YAML Post System** - Posts stored in `data/` folders  
✅ **Python Loader** - Reads and processes YAML files  
✅ **Jinja2 Templates** - Generates HTML from templates  
✅ **Build Script** - `src/build.py` generates static site  
✅ **GitHub Actions** - Auto-deploys on push to main  
✅ **Example Posts** - 6 dummy posts to get started  

## Workflow

### 1. Add a New Post

Create a YAML file in the appropriate folder:

```bash
# Event
data/events/event-003.yaml

# Information
data/info/info-003.yaml

# Advertisement
data/ads/ad-003.yaml
```

Use the schema from `docs/YAML_SCHEMA.md` as a template.

### 2. Build the Site

```bash
# Activate virtual environment
source venv/bin/activate

# Build
python src/build.py
```

This generates static HTML in the `docs/` folder.

### 3. Preview Locally

```bash
cd docs
python3 -m http.server 8000
# Open http://localhost:8000
```

### 4. Deploy

**Option A: Automatic (GitHub Actions)**
- Just push to main branch
- GitHub Actions will build and deploy automatically

**Option B: Manual**
```bash
python src/build.py
git add docs/
git commit -m "Update site"
git push
```

## File Structure

```
tavle/
├── data/              # Your YAML posts go here
│   ├── events/
│   ├── info/
│   └── ads/
├── src/
│   ├── loader.py      # YAML loader (don't modify unless needed)
│   └── build.py       # Build script (run this)
├── templates/          # HTML templates (modify to change design)
├── public/css/        # Styles (modify to change appearance)
└── docs/              # Generated HTML (auto-generated, don't edit directly)
```

## Tips

- **Unpublished posts**: Set `published: false` to hide from site
- **Expired posts**: Add `expires: YYYY-MM-DD` to auto-hide after date
- **Screen view**: Visit `/screen.html` for physical screen display
- **Tags**: Use tags to categorize posts (displayed at bottom of cards)

## Next Steps

1. Replace dummy posts with real content
2. Customize CSS in `public/css/style.css`
3. Modify templates in `templates/` if needed
4. Set up GitHub Pages (Settings → Pages → Source: GitHub Actions)

