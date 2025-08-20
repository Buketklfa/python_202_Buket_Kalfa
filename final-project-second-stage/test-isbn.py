from library import Library

def test_valid_isbn():
    lib = Library("test.json")
    book = lib.add_book("9780140328721")  # Matilda by Roald Dahl
    assert book is not None
    assert "Matilda" in book.title

def test_invalid_isbn():
    lib = Library("test.json")
    book = lib.add_book("0000000000000")
    assert book is None
