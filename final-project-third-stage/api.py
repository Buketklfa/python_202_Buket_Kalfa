from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from library import Library

app = FastAPI()
library = Library()

class ISBNRequest(BaseModel):
    isbn: str

@app.get("/books")
def get_books():
    return [book.__dict__ for book in library.list_books()]

@app.post("/books")
def add_book(req: ISBNRequest):
    book = library.add_book(req.isbn)
    if book:
        return book.__dict__
    raise HTTPException(status_code=404, detail="Kitap bulunamadı.")

@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    book = library.find_book(isbn)
    if book:
        library.remove_book(isbn)
        return {"message": "Kitap silindi."}
    raise HTTPException(status_code=404, detail="Kitap bulunamadı.")
