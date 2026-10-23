# Flask: Book Management REST API

Flask menyediakan routing dan utilitas HTTP dengan sedikit aturan bawaan.
Karena tidak memakai Pydantic, contoh ini memvalidasi body JSON **secara manual**.

## Arsitektur

```text
HTTP request
    -> Flask decorator (@app.get/post/put/delete)
    -> request.get_json() + validate_json_body()
    -> BookRepository (enkapsulasi state)
    -> Book dataclass
    -> jsonify() + status code
```

**Konsep OOP:** `BookRepository` menyimpan state di `_books`.
Endpoint tidak mengakses dictionary secara langsung. Melalui
`create_app(repository)`, aplikasi dapat menerima repository alternatif
untuk tes (**composition / dependency injection sederhana**).

## Menjalankan (Python 3.12+)

```bash
cd examples/web-frameworks/flask
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
flask --app app run --debug --port 8002
```

- API: http://127.0.0.1:8002/books
- Test: `python -m unittest discover -s tests -v`

Contoh:

```bash
curl -i -X POST http://127.0.0.1:8002/books \
  -H "Content-Type: application/json" \
  -d '{"title":"Clean Code","author":"Robert C. Martin"}'
curl -i http://127.0.0.1:8002/books/1
```

## Apa yang perlu diperhatikan?

- Validasi disusun manual di `validate_json_body`; input salah mendapat **400**.
- Flask tidak otomatis menghasilkan Swagger/OpenAPI dalam contoh ini.
- `app.test_client()` digunakan untuk test HTTP tanpa menjalankan server.
- Penyimpanan **in-memory**, hilang saat restart dan tidak mendukung multiworker;
  gunakan database/transaksi dan kontrol akses untuk aplikasi nyata.
