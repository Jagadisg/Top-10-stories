from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_top_news():    
    response = client.get("/api/hacker_news/top_10_stories/")
    assert response.status_code == 200
    