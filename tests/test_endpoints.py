from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_embedding():
    response = client.post("/api/v1/embed", json={"text": "This is a test sentence."})
    assert response.status_code == 200
    assert "embedding" in response.json()
