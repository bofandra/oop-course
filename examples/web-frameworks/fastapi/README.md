# FastAPI: Book Management REST API

FastAPI menonjolkan **type hints** dan validasi otomatis dengan **Pydantic**.
`BookInput` memvalidasi body JSON, `BookOutput` mendokumentasikan response,
dan `BookRepository` memegang state serta operasi penyimpanan.

## Arsitektur

```text
HTTP request
    -> FastAPI routing (@app.get/post/put/delete)
    -> Pydantic BookInput (validasi otomatis)
    -> BookRepository (enkapsulasi state & business operation)
    -> Book dataclass
    -> JSON response tervalidasi oleh BookOutput
```

**Konsep OOP:** `Book` adalah objek data; `BookRepository` adalah class
pemilik state `_books`; route functions adalah client dari repository
(**composition**); `create_app` memungkinkan repository berbeda pada setiap tes.

## Menjalankan (Python 3.12+)

```bash
cd examples/web-frameworks/fastapi
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
uvicorn app:app --reload --port 8001
```

- API: http://127.0.0.1:8001/books
- Swagger UI: http://127.0.0.1:8001/docs
- OpenAPI JSON: http://127.0.0.1:8001/openapi.json
- Test: `python -m unittest discover -s tests -v`

Contoh:

```bash
curl -i -X POST http://127.0.0.1:8001/books \
  -H "Content-Type: application/json" \
  -d '{"title":"Clean Code","author":"Robert C. Martin"}'
curl -i http://127.0.0.1:8001/books/1
```

## Apa yang perlu diperhatikan?

- Input salah mendapat HTTP **422** tanpa menulis parser JSON manual.
- `response_model` membuat skema respons terdokumentasi otomatis.
- Contoh ini memakai handler sinkron (`def`): `async def` hanya perlu
  ketika pekerjaan I/O-nya mendukung async, bukan sekadar demi tampilan.
- Penyimpanan **in-memory**, akan kosong lagi setelah restart, dan tidak aman
  untuk banyak worker/proses. Ini bukan desain produksi.
