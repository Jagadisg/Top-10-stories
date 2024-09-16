import httpx
from loguru import logger
from cachetools import TTLCache
from fastapi import HTTPException

from app.config import API_CONFIG_HACKERNEWS_STORIES_URL, API_CONFIG_HACKERNEWS_ITEM_URL
from .utils.utils_session import readable_time

news_cache = TTLCache(maxsize=100, ttl=300)

async def fetch_news_item(client: httpx.AsyncClient, item_id: int):
    try:
        if item_id in news_cache:
            logger.info(f"Serving news item {item_id} from cache")
            return news_cache[item_id] 
    except Exception as e:
        logger.error(e)
        
    try:
        item_url = f"{API_CONFIG_HACKERNEWS_ITEM_URL}{item_id}.json"
        response = await client.get(item_url)    
        response.raise_for_status()
        news_item = response.json()
        news_cache[item_id] = {
                "Title": news_item.get('title','Not Available'),
                "Author": news_item.get('by','Not Available'),
                "URL": news_item.get('url','Not Available'),
                "Score": news_item.get('score','Not Available'),            
                "Time": await readable_time(news_item.get('time','Not Available'))
            }
    except Exception as e:
        logger.error(e)
         
    logger.info(f"Fetched and cached news item {item_id}")
    return None
        
        
# @app.get("/")
# async def root():
#     return {"Greet":"Welcome to top hacker news"}       
        
        
async def topnews(client: httpx.AsyncClient):
    
    try:        
        logger.info(f"Fetching the top 10 stories")
        print(API_CONFIG_HACKERNEWS_STORIES_URL)
        response = await client.get(API_CONFIG_HACKERNEWS_STORIES_URL)
        print(response)
        response.raise_for_status()
        story_ids = response.json()[:10]
        
    except httpx.HTTPError as e:        
        logger.error(f"Error fetching top stories {e}")
        raise HTTPException(status_code=500, detail="Error fetching top stories") from e
    
    for item_id in story_ids:        
        try:            
            await fetch_news_item(client,item_id)            
            
        except httpx.HTTPError as e:            
            logger.error(f"Error fetching news {item_id}: {e}")
            
    logger.info(f"Returning {len(news_cache)} news items")
    
    return list(news_cache.values())