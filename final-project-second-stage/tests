import pytest
from library import Library

def test_list_books_empty():
    lib = Library("test_library.json")
    lib.books = []
    assert lib.list_books() == []

def test_find_book_not_found():
    lib = Library("test_library.json")
    lib.books = []
    assert lib.find_book("9999999999") is None
