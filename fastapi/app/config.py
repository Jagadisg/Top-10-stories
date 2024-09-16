import os


API_CONFIG_HACKERNEWS_STORIES_URL = os.getenv(
    "API_CONFIG_HACKERNEWS_STORIES_URL", "https://hacker-news.firebaseio.com/v0/topstories.json"
)

API_CONFIG_HACKERNEWS_ITEM_URL = os.getenv(
    "API_CONFIG_HACKERNEWS_ITEM_URL", "https://hacker-news.firebaseio.com/v0/item/"
)