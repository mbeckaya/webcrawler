import pytest
from queue import Queue

from crawler.url_frontier import UrlFrontier


TEST_URL = "https://www.google.de"

@pytest.fixture
def url_frontier() -> UrlFrontier:
    return UrlFrontier(Queue())

def test_add_valid_url_succeeds(url_frontier):
    assert url_frontier.add(TEST_URL) is True
    assert TEST_URL == url_frontier.get()

def test_add_duplicate_url_is_ignored(url_frontier):
    assert url_frontier.add(TEST_URL) is True
    assert url_frontier.add(TEST_URL) is False

    assert TEST_URL == url_frontier.get()
    assert None == url_frontier.get()

def test_add_invalid_string_fails(url_frontier):
    assert url_frontier.add("empty") is False


