from library import Library
from book import Book

def menu():
    print("1. Kitap Ekle")
    print("2. Kitap Sil")
    print("3. Kitapları Listele")
    print("4. ISBN ile Ara")
    print("5. Çıkış")

lib = Library()

while True:
    menu()
    choice = input("Seçiminiz: ")

    if choice == "1":
        title = input("Başlık: ")
        author = input("Yazar: ")
        isbn = input("ISBN: ")
        lib.add_book(Book(title, author, isbn))
    elif choice == "2":
        isbn = input("Silinecek ISBN: ")
        lib.remove_book(isbn)
    elif choice == "3":
        for book in lib.list_books():
            print(book.to_dict())
    elif choice == "4":
        isbn = input("Aranan ISBN: ")
        book = lib.find_book(isbn)
        print(book.to_dict() if book else "Kitap bulunamadı.")
    elif choice == "5":
        break
