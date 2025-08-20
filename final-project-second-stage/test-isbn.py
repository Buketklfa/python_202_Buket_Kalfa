from library import Library

def test_valid_isbn():
    lib = Library("test_library.json")
    book = lib.fetch_book_data("9780140328721")
    assert book is not None
    assert book.title != ""

def test_invalid_isbn():
    lib = Library("test_library.json")
    book = lib.fetch_book_data("0000000000000")
    assert book is None
