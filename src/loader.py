"""
YAML post loader utility.

Reads and parses YAML post files from data directories.
"""

import os
import yaml
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional


def load_yaml_file(file_path: Path) -> Optional[Dict[str, Any]]:
    """Load and parse a single YAML file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            if data:
                # Add file path for reference
                data['_file'] = str(file_path)
            return data
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
        return None


def is_post_expired(post: Dict[str, Any]) -> bool:
    """Check if a post has expired based on expires field."""
    if 'expires' not in post:
        return False
    
    try:
        expires_date = datetime.strptime(post['expires'], '%Y-%m-%d')
        return datetime.now() > expires_date
    except (ValueError, TypeError):
        return False


def load_posts_from_directory(directory: Path, post_type: str) -> List[Dict[str, Any]]:
    """Load all YAML posts from a directory."""
    posts = []
    
    if not directory.exists():
        print(f"Directory {directory} does not exist")
        return posts
    
    for file_path in directory.glob('*.yaml'):
        post = load_yaml_file(file_path)
        if post:
            # Ensure type is set
            post['type'] = post.get('type', post_type)
            # Filter out unpublished and expired posts
            if post.get('published', False) and not is_post_expired(post):
                posts.append(post)
    
    return posts


def load_all_posts(data_dir: Path = None) -> Dict[str, List[Dict[str, Any]]]:
    """
    Load all posts from data directories.
    
    Returns a dictionary with keys: 'events', 'info', 'ads'
    """
    if data_dir is None:
        # Assume we're in project root
        data_dir = Path(__file__).parent.parent / 'data'
    
    posts = {
        'events': load_posts_from_directory(data_dir / 'events', 'event'),
        'info': load_posts_from_directory(data_dir / 'info', 'info'),
        'ads': load_posts_from_directory(data_dir / 'ads', 'ad'),
    }
    
    # Sort posts by date (newest first)
    for post_type in posts:
        posts[post_type].sort(
            key=lambda x: x.get('date', ''),
            reverse=True
        )
    
    return posts


def get_all_posts_flat(posts_dict: Dict[str, List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
    """Get all posts as a flat list, sorted by date."""
    all_posts = []
    for post_list in posts_dict.values():
        all_posts.extend(post_list)
    
    all_posts.sort(
        key=lambda x: x.get('date', ''),
        reverse=True
    )
    
    return all_posts


if __name__ == '__main__':
    # Test the loader
    data_dir = Path(__file__).parent.parent / 'data'
    posts = load_all_posts(data_dir)
    
    print(f"Loaded {len(posts['events'])} events")
    print(f"Loaded {len(posts['info'])} info posts")
    print(f"Loaded {len(posts['ads'])} ads")
    
    all_posts = get_all_posts_flat(posts)
    print(f"\nTotal posts: {len(all_posts)}")
    
    for post in all_posts[:3]:
        print(f"\n- {post.get('title')} ({post.get('type')})")

