import json
from book import Book

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

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
