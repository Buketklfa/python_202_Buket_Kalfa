# python_202_Buket_Kalfa
# 📚 Python 202 Bootcamp - Kütüphane Yönetim Sistemi

Bu proje, **Global AI Hub Python 202 Bootcamp** kapsamında geliştirilmiş bir kütüphane yönetim uygulamasıdır. Proje, **terminal tabanlı bir uygulamadan** başlayıp, **harici API entegrasyonu** ve son olarak **FastAPI ile web tabanlı API’ye** dönüştürülerek üç aşamada geliştirilmiştir.  

Ayrıca, proje kapsamında **Python OOP prensipleri**, **JSON veri saklama**, **httpx ile API entegrasyonu**, **FastAPI ve Uvicorn**, **pytest ile test senaryoları** gibi ileri seviye teknikler uygulanmıştır.

---

## 🚀 Özellikler

### Aşama 1: Terminal Tabanlı Kütüphane
- Kitap ekleme ve silme
- Kütüphanedeki tüm kitapları listeleme
- ISBN ile kitap arama
- Verilerin **JSON dosyasında kalıcı olarak saklanması**
- Nesne Yönelimli Programlama (OOP) ile geliştirilmiş `Book` ve `Library` sınıfları
- Test senaryoları ile metod doğrulama (pytest)

### Aşama 2: Harici API ile Veri Zenginleştirme
- ISBN ile kitap ekleme (OpenLibrary API’den başlık ve yazar bilgisi çekilir)
- Hata yönetimi: geçersiz ISBN veya internet bağlantısı yoksa kullanıcı bilgilendirilir
- Aşama 1’in tüm özellikleri korunur
- `httpx` kullanılarak API çağrıları yapılır
- Testler güncellenmiş ve API entegrasyon testleri eklenmiştir

### Aşama 3: FastAPI ile Web Tabanlı API
- **HTTP Endpoint’leri:**
  - `GET /books` → Kütüphanedeki tüm kitapları listeler
  - `POST /books` → ISBN ile kitap ekler
  - `DELETE /books/{isbn}` → ISBN’e göre kitap siler
- Otomatik dokümantasyon: `/docs`
- `Pydantic` ile veri doğrulama
- `uvicorn` ile web sunucu çalıştırma
- Aşama 1 ve 2’nin tüm özellikleri korunur
- API testleri (pytest) eklenmiştir

---

## 🛠 Kullanılan Teknolojiler
- **Python 3.9+** → Ana programlama dili
- **JSON** → Kitap verilerinin saklanması
- **httpx** → Harici API çağrıları
- **FastAPI** → Web API geliştirme
- **Uvicorn** → FastAPI sunucusu
- **Pydantic** → Veri modelleri ve doğrulama
- **Pytest** → Test senaryoları
- **Terminal/CLI** → Aşama 1 ve 2 için kullanıcı arayüzü

---

## 📂 Proje Yapısı

### Aşama 1 (Terminal)
final-project-first-stage/
```
│
├── book.py # Book sınıfı
├── library.py # Library sınıfı
├── main.py # Terminal uygulaması
├── library.json # Kütüphane verileri
├── test_library.json # Test verileri
├── tests.py # Pytest testleri
├── requirements.txt # Bağımlılık dosyası (opsiyonel)
```


### Aşama 2 (API ile veri zenginleştirme)
final-project-second-stage/
```
├── book.py
├── library.py # OpenLibrary API entegrasyonu
├── main.py
├── library.json
├── test.json
├── test_library.json
├── test_library.py
├── test-isbn.py
├── tests.py
├── requirements.txt # httpx eklenmiş
```

### Aşama 3 (FastAPI)
final-project-third-stage/
```
├── api.py # FastAPI uygulaması
├── book.py
├── library.py
├── main.py
├── library.json
├── requirements.txt # fastapi, uvicorn, httpx
├── test_api.py
├── test-isbn.py
├── test_library.py
├── tests.py
├── test.json
└── test_library.json
```

---

## ⚙️ Kurulum ve Çalıştırma

### Terminal uygulaması (Aşama 1 & 2)
```bash
git clone <repo-link>
cd final-project-first-stage    # veya second-stage
pip install -r requirements.txt
python main.py                  # uygulamayı başlat
pytest                          # testleri çalıştır
```

###  FastAPI (Aşama 3)

```
git clone <repo-link>
cd final-project-third-stage
pip install -r requirements.txt
uvicorn api:app --reload         # API sunucusunu başlat
# API dokümantasyonu: http://127.0.0.1:8000/docs
pytest test_api.py
```


## ✍️ Proje Katkıları ve Öğrenilenler
Nesne yönelimli programlama ile proje yapısı oluşturma

JSON veri yönetimi ve kalıcılık

Harici API ile veri çekme ve doğrulama

Terminal ve web tabanlı kullanıcı arayüzü tasarlama

Test senaryoları yazma ve kod güvenliği sağlama

FastAPI ve Pydantic ile modern web API geliştirme

