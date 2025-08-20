import pytest
from book import Book
from library import Library

def test_add_and_find_book():
    lib = Library("test_library.json")
    lib.books = []
    book = Book("Test", "Tester", "123")
    lib.add_book(book)
    assert lib.find_book("123").title == "Test"

def test_remove_book():
    lib = Library("test_library.json")
    lib.books = [Book("Test", "Tester", "123")]
    lib.remove_book("123")
    assert lib.find_book("123") is None
