from library import Library
from book import Book

def test_add_and_find_book():
    lib = Library("test_library.json")
    book = Book("Test", "Tester", "123")
    lib.add_book(book)
    assert lib.find_book("123").title == "Test"
    lib.remove_book("123")
    
