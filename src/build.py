"""
Build script for generating static HTML from YAML posts.

Processes YAML files and renders Jinja2 templates to create static HTML.
"""

import os
import shutil
from pathlib import Path
from datetime import datetime, timedelta
from jinja2 import Environment, FileSystemLoader, select_autoescape
from loader import load_all_posts, get_all_posts_flat


def setup_build_environment():
    """Set up paths and directories."""
    project_root = Path(__file__).parent.parent
    templates_dir = project_root / 'templates'
    public_dir = project_root / 'public'
    output_dir = project_root / 'docs'  # GitHub Pages serves from /docs
    
    return project_root, templates_dir, public_dir, output_dir


def create_output_directory(output_dir: Path):
    """Create output directory and copy static assets."""
    # Create output directory
    output_dir.mkdir(exist_ok=True)
    
    # Copy static assets (CSS, JS, images)
    public_dir = output_dir.parent / 'public'
    if public_dir.exists():
        # Copy CSS
        css_output = output_dir / 'css'
        css_output.mkdir(exist_ok=True)
        for css_file in (public_dir / 'css').glob('*.css'):
            shutil.copy2(css_file, css_output / css_file.name)
        
        # Copy JS
        js_output = output_dir / 'js'
        js_output.mkdir(exist_ok=True)
        for js_file in (public_dir / 'js').glob('*.js'):
            shutil.copy2(js_file, js_output / js_file.name)
        
        # Copy any images or other assets
        for item in public_dir.iterdir():
            if item.is_file() and item.suffix in ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.ico']:
                shutil.copy2(item, output_dir / item.name)


def get_week_info(event_date_input):
    """Calculate week info for an event date."""
    try:
        # Handle both string and date objects
        if isinstance(event_date_input, str):
            event_date = datetime.strptime(event_date_input, '%Y-%m-%d')
            event_date_only = event_date.date()
        else:
            # Already a date object
            event_date_only = event_date_input
            event_date = datetime.combine(event_date_only, datetime.min.time())
        
        today = datetime.now().date()
        
        # Norwegian day names
        days = ['mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag', 'lørdag', 'søndag']
        day_name = days[event_date.weekday()]
        
        # Calculate weeks difference
        days_diff = (event_date_only - today).days
        weeks_diff = days_diff // 7
        
        if weeks_diff < 0:
            # For past events, still show the day name
            return f"({day_name})"
        elif weeks_diff == 0:
            return f"({day_name} denne uken)"
        elif weeks_diff == 1:
            return f"({day_name} neste uke)"
        else:
            return f"({day_name} om {weeks_diff} uker)"
    except (ValueError, TypeError) as e:
        print(f"Error calculating week info for {event_date_input}: {e}")
        return ""


def enrich_posts_with_week_info(posts_dict):
    """Add week info to event posts."""
    for post in posts_dict.get('events', []):
        if 'event_date' in post:
            week_info = get_week_info(post['event_date'])
            if week_info:  # Only add if not empty
                post['week_info'] = week_info


def build_site():
    """Main build function."""
    project_root, templates_dir, public_dir, output_dir = setup_build_environment()
    
    print("Building Tavla static site...")
    print(f"Templates: {templates_dir}")
    print(f"Output: {output_dir}")
    
    # Load posts
    data_dir = project_root / 'data'
    posts_by_type = load_all_posts(data_dir)
    
    # Enrich event posts with week info
    enrich_posts_with_week_info(posts_by_type)
    
    all_posts = get_all_posts_flat(posts_by_type)
    
    print(f"\nLoaded posts:")
    print(f"  - Events: {len(posts_by_type['events'])}")
    print(f"  - Info: {len(posts_by_type['info'])}")
    print(f"  - Ads: {len(posts_by_type['ads'])}")
    print(f"  - Total: {len(all_posts)}")
    
    # Set up Jinja2 environment
    env = Environment(
        loader=FileSystemLoader(str(templates_dir)),
        autoescape=select_autoescape(['html', 'xml'])
    )
    
    # Template context
    context = {
        'posts_by_type': posts_by_type,
        'all_posts': all_posts,
        'current_year': datetime.now().year,
    }
    
    # Create output directory and copy assets
    create_output_directory(output_dir)
    
    # Render templates
    print("\nRendering templates...")
    
    # Render index.html
    index_template = env.get_template('index.html')
    index_html = index_template.render(**context)
    (output_dir / 'index.html').write_text(index_html, encoding='utf-8')
    print("  ✓ index.html")
    
    # Render screen.html
    screen_template = env.get_template('screen.html')
    screen_html = screen_template.render(**context)
    (output_dir / 'screen.html').write_text(screen_html, encoding='utf-8')
    print("  ✓ screen.html")
    
    # Render kalender.html
    kalender_template = env.get_template('kalender.html')
    kalender_html = kalender_template.render(**context)
    (output_dir / 'kalender.html').write_text(kalender_html, encoding='utf-8')
    print("  ✓ kalender.html")
    
    print(f"\n✓ Build complete! Output in {output_dir}")
    print(f"\nTo preview locally:")
    print(f"  cd {output_dir}")
    print(f"  python3 -m http.server 8000")
    print(f"  Then open http://localhost:8000")


if __name__ == '__main__':
    build_site()

