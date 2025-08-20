import pytest
from book import Book
from library import Library

def test_add_and_find_book():
    lib = Library("test_library.json")
    lib.books = []
    book = Book("Test Kitap", "Test Yazar", "1111111111")
    lib.books.append(book)
    lib.save_books()
    found = lib.find_book("1111111111")
    assert found is not None
    assert found.title == "Test Kitap"

def test_remove_book():
    lib = Library("test_library.json")
    lib.books = [Book("Silinecek Kitap", "Yazar", "2222222222")]
    lib.save_books()
    lib.remove_book("2222222222")
    assert lib.find_book("2222222222") is None
