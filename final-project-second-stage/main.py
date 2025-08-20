from library import Library

def menu():
    print("\n1. ISBN ile Kitap Ekle\n2. Kitap Sil\n3. Kitapları Listele\n4. Kitap Ara\n5. Çıkış")

library = Library()

while True:
    menu()
    choice = input("Seçiminiz: ")

    if choice == "1":
        isbn = input("ISBN: ")
        book = library.add_book(isbn)
        print(book if book else "Kitap bulunamadı.")
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
