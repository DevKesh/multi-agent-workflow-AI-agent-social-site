#!/usr/bin/env python3
"""
Simple CLI tool to view the social feed without needing Streamlit.
Usage: python view_feed.py
"""
import json
import sys
import os

# Add current directory to path to import config
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# noinspection PyUnresolvedReferences
from config.settings import FEED_PATH


def view_feed():
    """Display all posts from the social feed in the terminal."""
    print("=" * 80)
    print("🤖 AI SOCIAL FEED - COMMAND LINE VIEWER")
    print("=" * 80)

    try:
        with open(FEED_PATH, 'r', encoding='utf-8') as f:
            feed = json.load(f)
            posts = feed.get('posts', [])

        if not posts:
            print("\n📭 No posts yet. Run 'python main.py' to generate content!\n")
            return

        print(f"\n📊 Total posts: {len(posts)}\n")
        print("-" * 80)

        # Display posts in reverse chronological order (newest first)
        for idx, post in enumerate(reversed(posts), 1):
            author = post.get('author', 'Unknown')
            text = post.get('text', '')
            print(f"\n#{idx} - 👤 {author}")
            print(f"{'─' * 80}")
            print(f"{text}")
            print(f"{'─' * 80}")

        print("\n" + "=" * 80)
        print("✨ End of feed")
        print("=" * 80)

    except FileNotFoundError:
        print(f"\n❌ Feed file not found: {FEED_PATH}")
        print("💡 Run 'python main.py' first to generate the feed!\n")
    except json.JSONDecodeError:
        print(f"\n❌ Invalid JSON in feed file: {FEED_PATH}")
        print("💡 The feed file may be corrupted. Check its contents.\n")
    except Exception as e:
        print(f"\n❌ Error reading feed: {e}\n")


if __name__ == "__main__":
    view_feed()
