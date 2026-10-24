# Flask — adapter HTTP minimal, OOP domain yang sama

> Pelajari dulu [pure Python](../00-pure-python/README.md) dan
> [OOP learning bridge](../OOP_LEARNING_BRIDGE.md).

## Fokus belajar: responsibility dan composition

`Flask` menyediakan router HTTP, `request.get_json()`, dan
`jsonify()`; business rules tidak ditempatkan pada route function.

~~~text
Flask @app.post("/books") -> parse_json_body()
                          -> BookService.create(title, author)
                          -> TitlePolicy + Book.validated_fields()
                          -> InMemoryBookRepository.create()
                          -> domain Book.to_dict() -> jsonify() + 201
~~~

Metode `parse_json_body()` hanya menangani bentuk HTTP request;
apakah title/author sah ditentukan oleh domain `Book`. Domain error
menjadi 400, `BookNotFound` menjadi 404.

## Kaitan dengan materi sebelumnya

- Modul 1–4: domain `Book`, state/behavior/invariant.
- Modul 5: `BookService` menggunakan repository lewat composition.
- Modul 6–7, 9: memory repository implements abstract contract.
- Modul 11: service dan repository memiliki referensi objek yang sama
  pada implementasi in-memory.
- Modul 12–13: paket domain dan domain exceptions.
- Modul 14–15: test domain berbeda dari HTTP integration test,
  dan reuse domain class saat framework berganti.

## Cara menjalankan (Python 3.12+)

~~~bash
cd examples/web-frameworks/flask
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
flask --app app run --debug --port 8002
~~~

~~~bash
curl -i -X POST http://127.0.0.1:8002/books \
  -H "Content-Type: application/json" \
  -d '{"title":"Clean Code","author":"Robert C. Martin"}'
python -m unittest discover -s tests -v
~~~

Jalankan command test dari terminal terpisah; tidak memerlukan
server aktif. `create_app(repository)` membuat state test terisolasi.

## Pertanyaan refleksi

1. Mengapa memindahkan `BookService` ke route menurunkan reusability?
2. Method apa yang benar-benar dipanggil saat `BookService.create()`?
3. Apa dampak mengganti repository pada `create_app`?
4. Bandingkan validasi Flask (HTTP parsing manual) dan FastAPI
   (Pydantic) tanpa mencampur keduanya dengan invariant domain.
5. Kapan abstraksi repository justru terlalu berat untuk aplikasi kecil?

> Tidak ada Swagger/OpenAPI otomatis dalam contoh Flask ini.
> In-memory persistence hanya demo lokal, bukan penyimpanan produksi.
