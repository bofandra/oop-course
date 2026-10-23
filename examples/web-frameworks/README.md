# Bonus praktikum: FastAPI, Flask, dan Django

> **Materi tambahan (opsional)** untuk pembelajar yang sudah memahami OOP.
> Web framework, HTTP/REST, database, dan dependency eksternal **bukan**
> capaian wajib atau bahan asesmen modul 0–16. Lihat [Source Boundary](../../SOURCE_BOUNDARY.md).

Ketiga proyek menjalankan **Book Management REST API** yang sama sehingga
perbandingan berfokus pada cara setiap framework menerima HTTP request,
memproses business logic, dan menghasilkan HTTP response.

## Tujuan pembelajaran

- Menghubungkan class, object, encapsulation, state, dan responsibility dengan backend web.
- Melihat perbedaan routing, request parsing, validation, persistence, dan pengujian.
- Memahami bahwa framework bukan pengganti desain OOP.

## Struktur

```text
examples/web-frameworks/
├── README.md                 # Panduan komparatif ini
├── fastapi/                  # Type hints, Pydantic, OpenAPI, in-memory repository
├── flask/                    # Minimal routing, validasi manual, in-memory repository
└── django/                   # Model ORM, migration, SQLite, view JSON native
```

## API yang dibandingkan (ketiga proyek sama)

| Method | Endpoint | Hasil | Status sukses |
|---|---|---|---|
| GET | /books | Semua buku | 200 |
| GET | /books/{id} | Satu buku | 200 |
| POST | /books | Membuat buku | 201 |
| PUT | /books/{id} | Mengubah seluruh field buku | 200 |
| DELETE | /books/{id} | Menghapus buku | 204 |

Format input untuk POST dan PUT:

```json
{"title": "Clean Code", "author": "Robert C. Martin"}
```

Format objek output:

```json
{"id": 1, "title": "Clean Code", "author": "Robert C. Martin"}
```

Seluruh field `title` dan `author` wajib berupa teks yang tidak kosong
(setelah whitespace dibuang), maksimal 120 karakter. ID dibuat server.
Respons input tidak valid adalah 422 (FastAPI) atau 400 (Flask/Django).
ID tidak ditemukan menghasilkan 404.

## Cara cepat menjalankan

Gunakan **Python 3.12+**. Jalankan dari direktori proyek masing-masing,
dan buat virtual environment terpisah agar dependensi tidak saling bertabrakan.

**FastAPI** — [baca panduan](fastapi/README.md):

```bash
cd examples/web-frameworks/fastapi
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
uvicorn app:app --reload --port 8001
```

Buka http://127.0.0.1:8001/docs untuk dokumentasi interaktif.

**Flask** — [baca panduan](flask/README.md):

```bash
cd examples/web-frameworks/flask
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
flask --app app run --debug --port 8002
```

**Django** — [baca panduan](django/README.md):

```bash
cd examples/web-frameworks/django
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8003
```

Di terminal terpisah, uji salah satu server (ganti port 8001 menjadi 8002/8003):

```bash
curl -i http://127.0.0.1:8001/books
curl -i -X POST http://127.0.0.1:8001/books \
  -H "Content-Type: application/json" \
  -d '{"title":"Clean Code","author":"Robert C. Martin"}'
curl -i http://127.0.0.1:8001/books/1
curl -i -X PUT http://127.0.0.1:8001/books/1 \
  -H "Content-Type: application/json" \
  -d '{"title":"Refactoring","author":"Martin Fowler"}'
curl -i -X DELETE http://127.0.0.1:8001/books/1
```

### Menjalankan tes

Jalankan dari direktori tiap proyek, setelah memasang `requirements.txt`:

```bash
# FastAPI / Flask
python -m unittest discover -s tests -v

# Django
python manage.py test books -v 2
```

GitHub Actions juga menjalankan ketiga suite melalui
[`web-framework-examples.yml`](../../.github/workflows/web-framework-examples.yml).

## Perbandingan arsitektur

```text
Client (curl/browser)
    |
    v
HTTP router / endpoint       <-- FastAPI / Flask / Django
    |
    v
Business objects & rules     <-- Book / BookRepository atau Book ORM
    |
    v
Storage                       <-- dict in-memory atau SQLite
    |
    v
JSON response + HTTP status
```

| Aspek | FastAPI | Flask | Django |
|---|---|---|---|
| Pemetaan URL | Decorator `@app.get/post/put/delete` | Decorator `@app.get/post/put/delete` | `urls.py` |
| Validasi input | `Pydantic` | Manual pada handler | Manual pada handler (tanpa Django REST Framework) |
| Model/domain | Dataclass `Book` | Dataclass `Book` | `models.Model` |
| Penyimpanan contoh | Dictionary dalam `BookRepository` | Dictionary dalam `BookRepository` | SQLite melalui ORM & migration |
| Dokumentasi OpenAPI | Otomatis di `/docs` | Tidak otomatis | Tidak otomatis |
| Konsep OOP | Composition: handler memakai repository | Composition: handler memakai repository | Model adalah class berbasis ORM |

**Catatan tentang keadilan perbandingan:** perbedaan penyimpanan disengaja.
FastAPI/Flask memakai state proses yang hilang saat server restart; Django
memakai SQLite yang bertahan setelah restart. Karena itu contoh ini **bukan**
benchmark performa maupun rekomendasi arsitektur produksi.

## Tugas praktikum lanjutan (opsional)

1. Tambahkan atribut `year` pada tiga implementasi dan ubah pengujiannya.
2. Jelaskan perbedaan validasi FastAPI, Flask, dan Django.
3. Ubah Flask/FastAPI agar menyimpan data ke database; bandingkan tanggung jawab handler.
4. Tambahkan autentikasi, otorisasi, rate limiting, dan konfigurasi aman jika proyek dikembangkan ke produksi.

## Peringatan keamanan dan operasional

Semua contoh disediakan untuk **belajar di lokal**: tanpa autentikasi, tanpa
otorisasi, tanpa pagination, tanpa audit log, dan tanpa deployment hardening.
Penggunaan untuk produksi memerlukan konfigurasi rahasia dari environment,
penanganan konkurensi/transaksi, database yang sesuai, dan proteksi request
(termasuk CSRF bila menggunakan autentikasi berbasis cookie).

## Bacaan dokumentasi resmi

- FastAPI: https://fastapi.tiangolo.com/
- Flask: https://flask.palletsprojects.com/
- Django: https://docs.djangoproject.com/
