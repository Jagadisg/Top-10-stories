import httpx
from loguru import logger
from fastapi import APIRouter, HTTPException, Depends

from starlette import status

from .hackernews import topnews
from .utils.utils_session import get_session

router = APIRouter(prefix="/hacker_news", tags=["hackernews"])


@router.get("/top_10_stories/")
async def top_ten_stories(client: httpx.AsyncClient = Depends(get_session)) -> list:
    try:
        result = await topnews(client=client)
        return result
    except Exception as e:
        logger.error(f"Error fetching top news: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Server Error"
        ) from e

