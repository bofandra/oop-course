# Ekstensi opsional: OOP ke FastAPI, Flask, dan Django

> **Mulai dari desain OOP, baru framework.** Ini materi praktik tambahan
> untuk yang telah menempuh modul 1–16. Tidak mengubah referensi formal,
> CLO, atau penilaian kursus utama.
> Lihat [Source Boundary](../../SOURCE_BOUNDARY.md).

## Mulai dari sini: jalur belajar

1. **[OOP_LEARNING_BRIDGE.md](OOP_LEARNING_BRIDGE.md)** —
   requirement → class diagram → objek → kolaborasi → adapter HTTP → testing.
2. **[OOP_CONCEPT_MAPPING.md](OOP_CONCEPT_MAPPING.md)** —
   relasi nyata ke modul 1–16, lengkap dengan path kode dan pertanyaan refleksi.
3. **[00-pure-python](00-pure-python/README.md)** —
   jalankan domain tanpa HTTP/server/database; ini baseline yang benar-benar
   diimpor oleh ketiga proyek web.
4. **[FastAPI](fastapi/README.md)** —
   pelajari Pydantic, route, OpenAPI, exception translation.
5. **[Flask](flask/README.md)** —
   bandingkan routing/parsing manual yang memakai service yang sama.
6. **[Django](django/README.md)** —
   belajar perbedaan ORM model dan domain entity melalui repository adapter.
7. **[Perbandingan arsitektur](ARCHITECTURE_COMPARISON.md)** —
   sequence diagram, dependency direction, identity & design trade-offs.
8. **[Latihan pemula](exercises/beginner.md)** →
   [menengah](exercises/intermediate.md) →
   [lanjut](exercises/advanced.md).
   Fasilitator: [INSTRUCTOR_EXTENSION_GUIDE.md](INSTRUCTOR_EXTENSION_GUIDE.md).

## Arsitektur: satu business core yang sama

~~~mermaid
flowchart TB
    FastAPI[FastAPI HTTP Adapter] --> Service
    Flask[Flask HTTP Adapter] --> Service
    Django[Django HTTP Adapter] --> Service
    Service[BookService] --> Book[Book domain: behavior & invariant]
    Service --> Repository[BookRepository ABC]
    Repository --> Memory[InMemoryBookRepository]
    Repository --> ORM[DjangoBookRepository]
    ORM --> Database[(SQLite via Django ORM)]
~~~

Diagram bersifat perbandingan: saat menjalankan satu aplikasi,
hanya adapter framework dan implementasi repository terkait yang aktif.
Paket pure Python (`book_domain`) tidak mengenal HTTP dan tidak
bergantung pada framework.

## Struktur folder

~~~text
examples/web-frameworks/
├── README.md
├── OOP_LEARNING_BRIDGE.md
├── OOP_CONCEPT_MAPPING.md
├── ARCHITECTURE_COMPARISON.md
├── INSTRUCTOR_EXTENSION_GUIDE.md
├── 00-pure-python/
│   ├── pyproject.toml, requirements.txt, demo.py, README.md
│   ├── src/book_domain/
│   │   ├── entities.py, errors.py, ports.py
│   │   ├── policies.py, services.py, memory.py
│   │   └── __init__.py
│   └── tests/
├── fastapi/        # API + tes HTTP: in-memory implementation
├── flask/          # API + tes HTTP: in-memory implementation
├── django/         # API + ORM repository + SQLite + tes integrasi
└── exercises/
    ├── beginner.md
    ├── intermediate.md
    └── advanced.md
~~~

## API: perilaku eksternal yang setara

| Method | Endpoint | Sukses |
|---|---|---|
| GET | /books | 200, array |
| GET | /books/{id} | 200, object; tidak ada = 404 |
| POST | /books | 201, object baru |
| PUT | /books/{id} | 200, object terubah; tidak ada = 404 |
| DELETE | /books/{id} | 204 tanpa body; tidak ada = 404 |

Input create/update:

~~~json
{"title":"Clean Code","author":"Robert C. Martin"}
~~~

Output:

~~~json
{"id":1,"title":"Clean Code","author":"Robert C. Martin"}
~~~

Domain: setiap title/author harus string 1–120 karakter setelah trim;
ID dibuat sistem dan bersifat read-only. HTTP input invalid menjadi
**422** di FastAPI, **400** di Flask/Django, sedangkan exception internal
tetap `BookValidationError`. Nilai yang tidak ditemukan memicu
`BookNotFound` di domain → **404** di adapter.

## Menjalankan (Python 3.12+)

**Dari root repository**: `git clone https://github.com/bofandra/oop-course.git`
kemudian `cd oop-course`. Gunakan virtualenv terpisah setiap contoh.

### 0. Pure Python — tanpa server

~~~bash
cd examples/web-frameworks/00-pure-python
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python demo.py
python -m unittest discover -s tests -v
~~~

Kembali ke root repo saat ingin membuka contoh lain.

### 1. FastAPI — port 8001

~~~bash
cd examples/web-frameworks/fastapi
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app:app --reload --port 8001
~~~

Dokumentasi interaktif: http://127.0.0.1:8001/docs

### 2. Flask — port 8002

~~~bash
cd examples/web-frameworks/flask
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
flask --app app run --debug --port 8002
~~~

### 3. Django — port 8003

~~~bash
cd examples/web-frameworks/django
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8003
~~~

Setiap `requirements.txt` memasang domain yang **sama** melalui
`-e ../00-pure-python`. Ketiga contoh menggunakan folder berdampingan
dalam clone repository; jangan salin salah satu folder saja.

### Uji API dari terminal lain

Ganti PORT menjadi 8001, 8002, atau 8003.

~~~bash
PORT=8001
curl -i "http://127.0.0.1:$PORT/books"
curl -i -X POST "http://127.0.0.1:$PORT/books" \
  -H "Content-Type: application/json" \
  -d '{"title":"Clean Code","author":"Robert C. Martin"}'
curl -i "http://127.0.0.1:$PORT/books/1"
curl -i -X PUT "http://127.0.0.1:$PORT/books/1" \
  -H "Content-Type: application/json" \
  -d '{"title":"Refactoring","author":"Martin Fowler"}'
curl -i -X DELETE "http://127.0.0.1:$PORT/books/1"
~~~

Di Windows PowerShell, sesuaikan deklarasi environment variable dan curl.

## Test suite & CI

- Pure Python, FastAPI, Flask:
  `python -m unittest discover -s tests -v` di masing-masing direktori.
- Django: `python manage.py test books -v 2` dari direktorinya,
  didahului `python manage.py migrate` saat menjalankan server.
- GitHub Actions `web-framework-examples.yml` menguji keempat target
  termasuk core, dan workflow kursus utama tetap terpisah.

## Tabel tanggung jawab

| Tanggung jawab | Kelas/komponen |
|---|---|
| Invariant data dan behavior | `book_domain.Book` |
| Abstraksi persistence | `book_domain.BookRepository(ABC)` |
| Use case / collaboration | `book_domain.BookService` |
| Variasi behavior | `TitlePolicy` subclasses (Strategy-style) |
| Penyimpanan memori | `InMemoryBookRepository` |
| Penyimpanan database | `DjangoBookRepository` + ORM Book |
| HTTP request/response | framework adapter masing-masing |

**OOP bukan sekadar banyak class**. Pertimbangkan apa yang berubah saat
domain rule berganti, framework diganti, atau penyimpanan berpindah.
Tidak semua aplikasi kecil membutuhkan port/service terpisah: itu salah
satu trade-off yang justru perlu dievaluasi mahasiswa.

## Batasan keamanan dan reproduktibilitas

Proyek bersifat edukatif **lokal saja**. Belum ada autentikasi, kontrol
akses, limit/pagination, audit trail, transaksi lintas-request, ataupun
pengamanan deployment. Penyimpanan in-memory tidak bertahan saat restart
atau lintas worker; Django SQLite adalah demo lokal. Contoh Django
memakai konfigurasi development dan CSRF exemption untuk unauthenticated
JSON API, **bukan pola untuk aplikasi produksi berbasis cookie/session**.

Dokumentasi resmi (pendukung teknologi, bukan referensi formal kursus):
[FastAPI](https://fastapi.tiangolo.com/),
[Flask](https://flask.palletsprojects.com/),
[Django](https://docs.djangoproject.com/).
