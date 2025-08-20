import json
import httpx
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
            json.dump([book.to_dict() for book in self.books], f, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()

    def list_books(self):
        return self.books

    def find_book(self, isbn):
        return next((book for book in self.books if book.isbn == isbn), None)

    def fetch_book_info(self, isbn):
        url = f"https://openlibrary.org/isbn/{isbn}.json"
        try:
            response = httpx.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                title = data.get("title", "Bilinmeyen Başlık")
                author = "Bilinmeyen Yazar"
                if "authors" in data:
                    author_key = data["authors"][0]["key"]
                    author_response = httpx.get(f"https://openlibrary.org{author_key}.json")
                    if author_response.status_code == 200:
                        author_data = author_response.json()
                        author = author_data.get("name", author)
                return Book(title, author, isbn)
            else:
                print("Kitap bulunamadı.")
                return None
        except httpx.RequestError:
            print("İnternet bağlantısı hatası.")
            return None

