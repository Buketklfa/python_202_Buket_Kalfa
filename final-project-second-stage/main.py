from library import Library

def menu():
    print("\n📚 Kütüphane Yönetim Sistemi")
    print("1. ISBN ile Kitap Ekle (API'den çek)")
    print("2. Kitap Sil")
    print("3. Kitapları Listele")
    print("4. ISBN ile Kitap Ara")
    print("5. Çıkış")

lib = Library()

while True:
    menu()
    choice = input("Seçiminiz: ")

    if choice == "1":
        isbn = input("ISBN girin: ")
        book = lib.fetch_book_info(isbn)
        if book:
            lib.add_book(book)
            print(f"✅ Kitap eklendi: {book.title} - {book.author}")
        else:
            print("❌ Kitap bilgisi alınamadı.")
    elif choice == "2":
        isbn = input("Silinecek ISBN: ")
        lib.remove_book(isbn)
        print("🗑️ Kitap silindi.")
    elif choice == "3":
        print("\n📖 Kütüphanedeki Kitaplar:")
        for book in lib.list_books():
            print(f"- {book.title} | {book.author} | {book.isbn}")
    elif choice == "4":
        isbn = input("Aranan ISBN: ")
        book = lib.find_book(isbn)
        if book:
            print(f"🔍 Bulundu: {book.title} - {book.author}")
        else:
            print("❌ Kitap bulunamadı.")
    elif choice == "5":
        print("👋 Çıkılıyor...")
        break
    else:
        print("⚠️ Geçersiz seçim.")
