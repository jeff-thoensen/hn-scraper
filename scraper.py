import requests
from bs4 import BeautifulSoup

def fetch_top_stories():
    url = "https://news.ycombinator.com"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select(".titleline > a")

    stories = []
    for link in links:
        title = link.get_text()
        href = link.get("href")
        stories.append({"title": title, "url": href})

    return stories

def sort_stories(stories, descending=False):
    return sorted(stories, key=lambda s: s["title"].lower(), reverse=descending)

if __name__ == "__main__":
    stories = fetch_top_stories()
    sorted_stories = sort_stories(stories, descending=False)  # Set to True for Z-A
    for i, story in enumerate(sorted_stories[:10], 1):
        print(f"{i}. {story['title']} ({story['url']})")