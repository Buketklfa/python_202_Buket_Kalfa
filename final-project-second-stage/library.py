import json
import httpx
from book import Book

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def fetch_book_data(self, isbn):
        try:
            response = httpx.get(f"https://openlibrary.org/isbn/{isbn}.json")
            if response.status_code == 200:
                data = response.json()
                title = data.get("title", "Bilinmiyor")
                authors = data.get("authors", [])
                author_names = ", ".join([a.get("name", "Bilinmiyor") for a in authors])
                return Book(title, author_names, isbn)
            else:
                return None
        except Exception:
            return None

    def add_book(self, isbn):
        book = self.fetch_book_data(isbn)
        if book:
            self.books.append(book)
            self.save_books()
            return book
        return None

    # Diğer metodlar aynı
