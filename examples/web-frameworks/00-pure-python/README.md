# 00 — Pure Python: memahami OOP sebelum web framework

## Mengapa baseline ini ada?

Membangun endpoint tidak otomatis berarti mendesain objek dengan baik.
Baca kode dari lapisan **domain**, baru ke web adapters:

1. `Book` = **entity** dengan identitas logis `id`, state privat-konvensional (`_title`, `_author`), behavior `revise()`, serta invariant.
2. `BookRepository(ABC)` = **abstract contract** untuk menyimpan/mencari buku.
3. `InMemoryBookRepository` = **inheritance** + overriding dari abstraksi.
4. `BookService` = **composition**: memiliki relasi ke repository dan policy tanpa mengetahui teknologi penyimpanan.
5. `TitlePolicy` = **polymorphism / Strategy-style**: normalisasi dapat diganti tanpa mengubah service.
6. Exceptions `BookValidationError` dan `BookNotFound` = **domain contract**, bukan kode HTTP.

## Diagram class

~~~mermaid
classDiagram
class Book {
  -int _id
  -str _title
  -str _author
  +revise(title, author)
  +rename(title)
  +to_dict()
}
class BookRepository {
  <<abstract>>
  +list()
  +get(id)
  +create(title, author)
  +save(book)
  +delete(id)
}
class InMemoryBookRepository
class BookService
class TitlePolicy {
  <<abstract>>
  +normalize(title)
}
class KeepCaseTitlePolicy
class CompactWhitespaceTitlePolicy
BookRepository <|-- InMemoryBookRepository
TitlePolicy <|-- KeepCaseTitlePolicy
TitlePolicy <|-- CompactWhitespaceTitlePolicy
BookService --> BookRepository : uses
BookService --> TitlePolicy : uses
BookRepository --> Book : stores
~~~

## Menjalankan

Gunakan Python 3.12+ dari direktori ini:

~~~bash
cd examples/web-frameworks/00-pure-python
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python demo.py
python -m unittest discover -s tests -v
~~~

**Tidak membutuhkan Flask, FastAPI, Django, HTTP server, atau database.**

## Jejak objek saat create()

1. Caller membangun `InMemoryBookRepository()`, lalu `BookService(repository)`.
2. `BookService.create(title, author)` minta policy menormalisasi judul.
3. `Book.validated_fields()` memeriksa input sebelum penyimpanan.
4. `repository.create()` membuat instansi `Book` dan memberi ID.
5. Buku dikembalikan sebagai objek dengan public methods/properties.

Saat `update()`, `Book.revise()` memvalidasi kedua field **sebelum**
mengubah state. Ini menjaga invariant dan mencegah perubahan setengah jalan.

## Hubungan dengan modul wajib

- Modul 1–3: entity, class, instance, state, method, identity.
- Modul 4–5: encapsulation dan relasi client–supplier (**has-a**).
- Modul 6–7, 9: subclass, overriding, abstract class, polymorphism.
- Modul 11: identity vs alias/reference: `repo.get(1) is book` pada memory adapter.
- Modul 12–13: modul Python, exceptions, invariant.
- Modul 14–15: OOA → OOD → OOP → OOT, tanggung jawab dan Strategy-style.
- Modul 16: fondasi untuk solusi final yang dapat diperluas.

Baca [matriks modul](../OOP_CONCEPT_MAPPING.md) dan
[peta pembelajaran](../OOP_LEARNING_BRIDGE.md).

## Latihan refleksi

1. Mengapa HTTP tidak muncul dalam `BookService`?
2. Mengapa properti `id` hanya bisa dibaca?
3. Jika objek `Book` telah diubah langsung melalui alias dari repository
   in-memory, apakah `save()` masih diperlukan? Bandingkan dengan Django ORM.
4. Mengapa membuat 10 subclass berbeda untuk 10 judul buku adalah desain buruk?
5. Apa dampak mengubah penyimpanan dari dictionary menjadi database terhadap
   `BookService`, jika abstraksi repository dipertahankan?

## Batasan contoh

`InMemoryBookRepository` tidak persisten maupun thread/process-safe.
Referensi `Book` dapat ter-alias antar pemanggil; contoh ini sengaja
memperlihatkan konsekuensi lifecycle dan reference pada Modul 11.
Untuk sistem nyata gunakan transaksi, isolasi, dan batas aggregate sesuai kebutuhan.
