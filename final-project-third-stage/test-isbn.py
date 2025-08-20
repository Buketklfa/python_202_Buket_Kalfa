from library import Library
from book import Book

def test_add_book_by_isbn():
    lib = Library("test_library.json")
    book = Book("Test Kitap", "Test Yazar", "1111111111")
    lib.add_book(book)
    assert lib.find_by_isbn("1111111111") is not None
