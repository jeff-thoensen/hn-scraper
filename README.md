# HN Scraper

This is a quick Python script that scrapes top stories from Hacker News and sorts them by title. Nothing fancy — just trying out some test coverage and GitHub Actions.

### What it does

- Scrapes the front page of Hacker News
- Returns a list of titles + URLs
- Lets you sort alphabetically
- Tests are written with pytest
- Network call is mocked so tests don’t hit the real site

### To run it

```bash
python scraper.py
```
