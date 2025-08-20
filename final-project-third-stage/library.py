import json
from book import Book

class Library:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r") as f:
                return [Book(**data) for data in json.load(f)]
        except FileNotFoundError:
            return []

    def save_books(self):
        with open(self.filename, "w") as f:
            json.dump([book.to_dict() for book in self.books], f, indent=2)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()

    def get_all_books(self):
        return self.books

    def find_by_isbn(self, isbn):
        return next((book for book in self.books if book.isbn == isbn), None)
