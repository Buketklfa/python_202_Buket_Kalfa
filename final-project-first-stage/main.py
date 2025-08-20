from library import Library
from book import Book

def menu():
    print("\n1. Kitap Ekle\n2. Kitap Sil\n3. Kitapları Listele\n4. Kitap Ara\n5. Çıkış")

library = Library()

while True:
    menu()
    choice = input("Seçiminiz: ")

    if choice == "1":
        title = input("Kitap Başlığı: ")
        author = input("Yazar: ")
        isbn = input("ISBN: ")
        book = Book(title, author, isbn)
        library.add_book(book)
        print("Kitap eklendi.")
    elif choice == "2":
        isbn = input("Silinecek ISBN: ")
        library.remove_book(isbn)
        print("Kitap silindi.")
    elif choice == "3":
        for book in library.list_books():
            print(book)
    elif choice == "4":
        isbn = input("Aranan ISBN: ")
        book = library.find_book(isbn)
        print(book if book else "Kitap bulunamadı.")
    elif choice == "5":
        break
    else:
        print("Geçersiz seçim.")
