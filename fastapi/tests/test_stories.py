import pytest
import httpx
import logging

from app.hackernews.utils.utils_session import readable_time, get_session

logging.basicConfig(level=logging.DEBUG)

@pytest.mark.asyncio
async def test_readable_time():
    logging.debug("Running test_readable_time")
    
    timestamp = 1633046400 
    expected_result = "2021-10-01 00:00:00"
    result = await readable_time(timestamp)
    logging.debug(f"Result: {result}, Expected: {expected_result}")
    assert result == expected_result
    
    timestamp = "Not Available"
    result = await readable_time(timestamp)
    logging.debug(f"Result: {result}, Expected: None")
    assert result is None
    
@pytest.mark.asyncio    
async def test_get_session():
    logging.debug("Running test_get_session")
    
    async for session in get_session():
        assert isinstance(session, httpx.AsyncClient)
        response = await session.get("https://jsonplaceholder.typicode.com/todos/1")
        logging.debug(f"Response status code: {response.status_code}")
        assert response.status_code == 200
