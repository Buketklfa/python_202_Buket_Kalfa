import httpx
from book import Book

class Library:
    # önceki kodlar...

    def fetch_book_info(self, isbn):
        url = f"https://openlibrary.org/isbn/{isbn}.json"
        try:
            response = httpx.get(url)
            if response.status_code == 200:
                data = response.json()
                return Book(data["title"], data.get("authors", [{}])[0].get("name", "Unknown"), isbn)
            else:
                print("Kitap bulunamadı.")
        except httpx.RequestError:
            print("İnternet bağlantısı yok.")
