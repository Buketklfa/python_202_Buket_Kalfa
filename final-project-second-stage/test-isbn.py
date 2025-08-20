from library import Library

def test_fetch_valid_isbn():
    lib = Library("test.json")
    book = lib.fetch_book_info("9780140328721")  # Matilda by Roald Dahl
    assert book is not None
    assert book.title.lower().startswith("matilda")

def test_fetch_invalid_isbn():
    lib = Library("test.json")
    book = lib.fetch_book_info("0000000000000")  # Geçersiz ISBN
    assert book is None
