from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200

def test_add_invalid_isbn():
    response = client.post("/books", params={"isbn": "0000000000"})
    assert response.status_code == 404
