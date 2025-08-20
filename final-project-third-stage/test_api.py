from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200

def test_post_book():
    response = client.post("/books", json={"isbn": "9780140328721"})
    assert response.status_code in [200, 404]

def test_delete_book():
    response = client.delete("/books/9780140328721")
    assert response.status_code in [200, 404]
