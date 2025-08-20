from library import Library
from book import Book

def test_remove_book():
    lib = Library("test_library.json")
    lib.add_book(Book("Silinecek", "Yazar", "2222222222"))
    lib.remove_book("2222222222")
    assert lib.find_by_isbn("2222222222") is None
