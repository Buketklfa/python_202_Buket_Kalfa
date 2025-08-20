import json
import httpx
from book import Book

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def fetch_book_data(self, isbn):
        url = f"https://openlibrary.org/isbn/{isbn}.json"
        try:
            response = httpx.get(url)
            if response.status_code == 200:
                data = response.json()
                title = data.get("title", "Bilinmeyen")
                authors = data.get("authors", [])
                author_names = ", ".join([a.get("name", "Anonim") for a in authors])
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

    def remove_book(self, isbn):
        self.books = [b for b in self.books if b.isbn != isbn]
        self.save_books()

    def list_books(self):
        return self.books

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def load_books(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.books = [Book(**item) for item in data]
        except FileNotFoundError:
            self.books = []

    def save_books(self):
        with open(self.filename, "w") as f:
            json.dump([book.__dict__ for book in self.books], f, indent=4)
