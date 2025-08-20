from fastapi import FastAPI, HTTPException
from library import Library
from book import Book
import httpx

app = FastAPI()
library = Library()

@app.get("/books")
def get_books():
    return [book.to_dict() for book in library.get_all_books()]

@app.post("/books")
def add_book(isbn: str):
    url = f"https://openlibrary.org/isbn/{isbn}.json"
    try:
        response = httpx.get(url)
        response.raise_for_status()
        data = response.json()
        title = data.get("title", "Unknown Title")
        author = data.get("authors", [{"name": "Unknown Author"}])[0]["name"]
        book = Book(title, author, isbn)
        library.add_book(book)
        return book.to_dict()
    except httpx.HTTPError:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı")

@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    book = library.find_by_isbn(isbn)
    if not book:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı")
    library.remove_book(isbn)
    return {"message": "Kitap silindi"}
