import pytest
from book import Book
from library import Library

@pytest.fixture
def test_library():
    lib = Library("test_library.json")
    lib.books = []  # Test için temiz başlangıç
    return lib

def test_add_book(test_library):
    book = Book("Test Book", "Test Author", "1234567890")
    test_library.add_book(book)
    assert test_library.find_book("1234567890") is not None

def test_remove_book(test_library):
    book = Book("Test Book", "Test Author", "1234567890")
    test_library.add_book(book)
    test_library.remove_book("1234567890")
    assert test_library.find_book("1234567890") is None

def test_list_books(test_library):
    book1 = Book("Book One", "Author A", "111")
    book2 = Book("Book Two", "Author B", "222")
    test_library.add_book(book1)
    test_library.add_book(book2)
    books = test_library.list_books()
    assert len(books) == 2

def test_find_book(test_library):
    book = Book("Find Me", "Author C", "333")
    test_library.add_book(book)
    found = test_library.find_book("333")
    assert found.title == "Find Me"
