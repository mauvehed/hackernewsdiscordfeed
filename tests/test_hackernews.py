"""
This module contains tests for the hackernews module.
"""

import pytest
from hackernewsdiscordfeed.hackernews import fetch_hacker_news_stories

@pytest.mark.asyncio
async def test_fetch_hacker_news_stories(monkeypatch):
    """
    Tests the fetch_hacker_news_stories function by mocking the requests.get method.

    Args:
        monkeypatch: pytest's monkeypatch fixture for modifying functions during the test.
    """
    def mock_requests_get(url):
        if url == 'https://hacker-news.firebaseio.com/v0/beststories.json':
            return MockResponse([1, 2], 200)
        elif url.startswith('https://hacker-news.firebaseio.com/v0/item/'):
            return MockResponse(
                {
                    "title": "Test Story",
                    "score": 100,
                    "url": "https://example.com/test"
                }, 200
            )
        return MockResponse(None, 404)

    class MockResponse:
        """
        A mock response class to mimic the behavior of the response object returned by requests.get.
        """
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    monkeypatch.setattr("requests.get", mock_requests_get)
    
    stories = await fetch_hacker_news_stories()
    assert len(stories) == 2
    assert stories[0]['title'] == "Test Story"
    assert stories[1]['title'] == "Test Story"
