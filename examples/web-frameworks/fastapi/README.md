# FastAPI — adapter HTTP untuk OOP domain yang sama

> Baca dahulu: [pure Python](../00-pure-python/README.md),
> [learning bridge](../OOP_LEARNING_BRIDGE.md), dan
> [mapping OOP 1–16](../OOP_CONCEPT_MAPPING.md).

## Fokus belajar: validasi request bukan model domain

- `book_domain.Book`: domain entity, invariant, behavior.
- `BookInput(BaseModel)`: bentuk input HTTP, divalidasi Pydantic.
- `BookOutput(BaseModel)`: bentuk output HTTP/OpenAPI; bukan domain class.
- `BookService`: method yang merepresentasikan use case CRUD.
- `InMemoryBookRepository(BookRepository)`: penyimpanan tanpa database.
- `create_app(repository)`: **composition root**, menyuntikkan
  implementasi repository sehingga tests mengisolasi state.

### Kolaborasi objek saat POST /books

~~~text
JSON -> Pydantic BookInput -> create_book()
     -> BookService.create() -> TitlePolicy.normalize()
     -> Book.validated_fields() -> InMemoryBookRepository.create()
     -> domain Book -> Book.to_dict()
     -> BookOutput schema -> JSON 201
~~~

Handler **tidak** menyusun ulang aturan validitas domain.
Input HTTP tidak valid → 422 otomatis dari Pydantic; error domain tetap
diterjemahkan ke 422, dan `BookNotFound` menjadi 404.

## Kaitan ke materi sebelumnya

| Modul | Evidensi kode |
|---|---|
| 2–4 | objek `Book`, state `_title`, invariant `revise` |
| 5 | `create_app` menyusun service dan repository (has-a) |
| 7 & 9 | repository konkret memenuhi abstract repository |
| 11 | objek Book yang disimpan in-memory dapat ter-alias |
| 12 | import `book_domain` sebagai paket eksternal |
| 13 | domain exception diterjemahkan pada boundary HTTP |
| 14–15 | test domain vs test HTTP adapter; reuse lintas framework |

Peta lengkap per modul: [OOP_CONCEPT_MAPPING.md](../OOP_CONCEPT_MAPPING.md).

## Cara menjalankan (Python 3.12+)

Dari folder repository, masuk ke:

~~~bash
cd examples/web-frameworks/fastapi
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
uvicorn app:app --reload --port 8001
~~~

Lihat http://127.0.0.1:8001/docs untuk Swagger UI dan
http://127.0.0.1:8001/openapi.json untuk skema.

~~~bash
curl -i -X POST http://127.0.0.1:8001/books \
  -H "Content-Type: application/json" \
  -d '{"title":"Clean Code","author":"Robert C. Martin"}'
python -m unittest discover -s tests -v
~~~

Run command test pada terminal kedua setelah install (tidak harus
sambil menjalankan server).

## Diskusi refleksi

1. Mengapa `BookInput` bukan subclass domain `Book`?
2. Apa dampaknya jika `BookService` memanggil `HTTPException`?
3. Mengapa `create_app(repository)` memudahkan unit/integration testing?
4. Jika Pydantic memastikan judul non-empty, mengapa domain tetap
   memvalidasi judulnya sendiri?
5. Apakah `async def` otomatis lebih cepat daripada `def`?
   Contoh ini menggunakan handler sinkron untuk operasi sinkron.

> Perhatian: state in-memory lokal hilang setelah proses restart, dan
> tidak dirancang untuk worker/concurrency atau produksi.
