# Django: Book Management REST API

Django memakai `Book(models.Model)` yang sekaligus mendeskripsikan data
dan menjadi pintu masuk **ORM**. Data contoh tersimpan dalam **SQLite**.
Untuk perbandingan langsung dengan FastAPI/Flask, HTTP API dibuat memakai
**Django native views**, tanpa Django REST Framework.

## Arsitektur

```text
HTTP request
    -> config/urls.py -> books/urls.py
    -> books/views.py (JSON parsing & validasi)
    -> books/models.py: Book(models.Model)
    -> Django ORM -> SQLite (db.sqlite3)
    -> JsonResponse()
```

**Konsep OOP:** `Book` adalah subclass dari `models.Model`
(**inheritance**); instansinya menggabungkan state dan behavior seperti
`save()` / `delete()`. Views memakai objek ORM, bukan menulis SQL manual.

## Menjalankan (Python 3.12+)

```bash
cd examples/web-frameworks/django
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8003
```

- API: http://127.0.0.1:8003/books
- Pengujian: `python manage.py test books -v 2` (database tes terisolasi).
- Cek perubahan model: `python manage.py makemigrations --check --dry-run`.

Contoh:

```bash
curl -i -X POST http://127.0.0.1:8003/books \
  -H "Content-Type: application/json" \
  -d '{"title":"Clean Code","author":"Robert C. Martin"}'
curl -i http://127.0.0.1:8003/books/1
```

## Apa yang perlu diperhatikan?

- `manage.py migrate` harus dijalankan sebelum memakai API.
- Model menyatakan field; migrasi `0001_initial.py` membuat tabel.
- Validasi JSON diprogram manual; tanpa DRF tidak ada serializer otomatis
  dan error input contoh ini menghasilkan **400**.
- Django mendukung fitur yang lebih luas daripada yang ditampilkan oleh
  proyek mini ini, seperti autentikasi, permissions, forms, admin, dan ORM.
- View `POST/PUT/DELETE` di sini menggunakan `csrf_exempt` **hanya untuk
  demonstrasi JSON API tanpa login/cookie**. Jangan memakai pendekatan ini
  untuk endpoint produksi yang mengandalkan sesi/cookie.
- `SECRET_KEY`, `DEBUG=True`, dan SQLite di sini untuk lokal saja;
  bukan konfigurasi deployment.
