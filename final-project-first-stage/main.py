from library import Library
from book import Book

lib = Library()

def menu():
    while True:
        print("\n1. Kitap Ekle\n2. Kitap Sil\n3. Kitapları Listele\n4. Kitap Ara\n5. Çıkış")
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
                print(book)
        elif choice == "4":
            isbn = input("Aranacak ISBN: ")
            book = lib.find_book(isbn)
            print(book if book else "Kitap bulunamadı.")
        elif choice == "5":
            break
        else:
            print("Geçersiz seçim.")
