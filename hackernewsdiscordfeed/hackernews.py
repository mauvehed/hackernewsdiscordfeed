"""
This module defines functions to fetch the latest best stories from Hacker News.
"""

import requests
from typing import List, Dict, Any

async def fetch_hacker_news_stories() -> List[Dict[str, Any]]:
    """
    Fetches the latest best stories from Hacker News.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries containing story details.
    """
    url = 'https://hacker-news.firebaseio.com/v0/beststories.json'
    story_ids = requests.get(url).json()
    stories = []
    for story_id in story_ids[:5]:
        story_url = f'https://hacker-news.firebaseio.com/v0/item/{story_id}.json'
        story = requests.get(story_url).json()
        stories.append(story)
    return stories
