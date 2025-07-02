from scraper import fetch_top_stories
from scraper import sort_stories
from unittest.mock import patch

FAKE_HTML = """
<html>
  <body>
    <tr class="athing">
      <td class="title">
        <span class="titleline">
          <a href="https://example.com/story1">Example Story 1</a>
        </span>
      </td>
    </tr>
    <tr class="athing">
      <td class="title">
        <span class="titleline">
          <a href="https://example.com/story2">Example Story 2</a>
        </span>
      </td>
    </tr>
  </body>
</html>
"""

@patch("scraper.requests.get")
def test_fetch_top_stories_returns_expected_data(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = FAKE_HTML

    stories = fetch_top_stories()

    assert isinstance(stories, list)
    assert len(stories) == 2
    assert stories[0]["title"] == "Example Story 1"
    assert stories[0]["url"] == "https://example.com/story1"
    assert stories[1]["title"] == "Example Story 2"
    assert stories[1]["url"] == "https://example.com/story2"

def test_sort_stories_sorts_by_title_ascending():
    stories = [
        {"title": "Zebra article", "url": "https://z.com"},
        {"title": "apple article", "url": "https://a.com"},
        {"title": "Banana article", "url": "https://b.com"},
    ]

    sorted_stories = sort_stories(stories, descending=False)

    titles = [s["title"] for s in sorted_stories]
    assert titles == ["apple article", "Banana article", "Zebra article"]

def test_sort_stories_sorts_by_title_descending():
    stories = [
        {"title": "Zebra article", "url": "https://z.com"},
        {"title": "apple article", "url": "https://a.com"},
        {"title": "Banana article", "url": "https://b.com"},
    ]

    sorted_stories = sort_stories(stories, descending=True)

    titles = [s["title"] for s in sorted_stories]
    assert titles == ["Zebra article", "Banana article", "apple article"]

