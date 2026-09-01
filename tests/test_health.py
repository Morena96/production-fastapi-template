from fastapi.testclient import TestClient

from app.main import app


def test_live_healthcheck():
    client = TestClient(app)
    response = client.get("/health/live")
    assert response.status_code == 200
    assert response.json() == {"status": "alive"}
