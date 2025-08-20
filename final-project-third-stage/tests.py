from book import Book

def test_book_to_dict():
    book = Book("Başlık", "Yazar", "123")
    assert book.to_dict() == {
        "title": "Başlık",
        "author": "Yazar",
        "isbn": "123"
    }
