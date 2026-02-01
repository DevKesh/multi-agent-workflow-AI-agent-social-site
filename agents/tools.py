import json
import sys
import os
from datetime import datetime
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
# noinspection PyUnresolvedReferences
from config.settings import FEED_PATH

def post_to_site(author: str, text: str) -> str:
    """Append a post to the site feed with timestamp."""
    with open(FEED_PATH, 'r+', encoding='utf-8') as f:
        feed = json.load(f)
        post = {
            'author': author,
            'text': text,
            'timestamp': datetime.now().isoformat()
        }
        feed.setdefault('posts', []).append(post)
        f.seek(0)
        json.dump(feed, f, ensure_ascii=False, indent=2)
        f.truncate()
    return f"✅ Posted by {author}: {text[:50]}..."

def read_site_feed() -> str:
    """Read all posts from the site feed."""
    with open(FEED_PATH, 'r', encoding='utf-8') as f:
        feed = json.load(f)
        posts = feed.get('posts', [])
        return f"Feed has {len(posts)} posts"
