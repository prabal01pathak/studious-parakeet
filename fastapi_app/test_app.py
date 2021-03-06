from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_root():
    res = client.get('/')
    assert res.status_code == 200
    assert res.json() == {"message": "Hello World"}
