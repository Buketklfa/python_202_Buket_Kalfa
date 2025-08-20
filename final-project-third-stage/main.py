from library import Library
from book import Book

lib = Library()
lib.add_book(Book("Deneme Kitabı", "Yazar", "1234567890"))
print([book.to_dict() for book in lib.get_all_books()])
