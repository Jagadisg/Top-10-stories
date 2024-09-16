import httpx
from datetime import datetime


async def get_session():
    
    async with httpx.AsyncClient() as session:
        yield session
        
        
async def readable_time(timestamp):
    
    if timestamp != "Not Available":
        date_obj = datetime.fromtimestamp(timestamp)
        readable_format = date_obj.strftime("%Y-%m-%d %H:%M:%S")    
        return readable_format
