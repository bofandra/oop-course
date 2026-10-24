# Dari Modul 1–16 menuju Web API: belajar OOP terlebih dahulu

> **Praktikum ekstensi opsional**, bukan materi wajib/asesmen kursus.
> Tetap gunakan dua sumber formal dan batasan capaian pada
> [SOURCE_BOUNDARY.md](../../SOURCE_BOUNDARY.md).

## Pertanyaan pengarah

**Jika framework diganti, bagian kode manakah yang seharusnya tetap benar?**

Jawabannya: konsep domain dan aturan bisnis tidak seharusnya bergantung pada
Flask, FastAPI, atau Django. Karena itu kita mulai dari
[00-pure-python](00-pure-python/README.md) dan benar-benar **memakainya ulang**
dalam ketiga framework, bukan menulis tiga versi aturan bisnis yang berbeda.

## Prasyarat terhubung ke modul sebelumnya

| Sebelum praktik | Pahami dari kursus wajib | Bukti yang dapat ditunjukkan |
|---|---|---|
| Modul 1–3 | class, instance, state, behavior, identity | `Book` dibuat melalui `Book(id, title, author)` |
| Modul 4–5 | encapsulation, hubungan client–supplier | `BookService` punya kolaborator `BookRepository` |
| Modul 6–7, 9 | inheritance, polymorphism, ABC | `InMemoryBookRepository` dan `DjangoBookRepository` menerapkan kontrak yang sama |
| Modul 11–13 | identity/reference, module, exception | alias in-memory, `BookNotFound`, `BookValidationError` |
| Modul 14–15 | OOA/OOD/OOP/OOT, reuse | klasifikasi responsibility, diagram, unit tests |
| Modul 16 | final solution | menerapkan desain yang bisa ditukar adapter-nya |

Untuk pemetaan **setiap modul 1–16**, lihat [OOP_CONCEPT_MAPPING.md](OOP_CONCEPT_MAPPING.md).

## Tahap 1 — Kebutuhan, bukan framework (OOA)

Tentukan kebutuhan fungsional terlebih dulu:

- Membuat buku berjudul dan bernama pengarang yang valid;
- Mendapatkan semua buku dan buku tertentu;
- Mengubah judul/pengarang tanpa mengorbankan invariant;
- Menghapus buku dan menangani buku yang tidak ditemukan.

Kontrak domain yang perlu dipertahankan:

- ID positif diberikan sistem dan tidak diganti setelah dibuat;
- Judul dan pengarang: string, tidak kosong setelah trim, maksimum 120 karakter;
- `revise(title, author)` harus memvalidasi *keduanya lebih dahulu*
  sebelum state berubah (object-level all-or-nothing);
- Buku yang tidak ditemukan memicu `BookNotFound`;
- Error domain **tidak mengenal HTTP 404/422**.

Perhatikan perbedaan *requirement* vs *implementation choice*.
API dengan JSON adalah pilihan antarmuka, bukan identitas dari sebuah `Book`.

## Tahap 2 — Mendesain class (OOD)

~~~mermaid
classDiagram
class Book {
  -int _id
  -str _title
  -str _author
  +revise(title,author)
  +rename(title)
  +to_dict()
}
class BookService {
  -BookRepository _repository
  -TitlePolicy _title_policy
  +create(title,author)
  +get(id)
  +list()
  +update(id,title,author)
  +delete(id)
}
class BookRepository {
  <<abstract>>
  +get(id)
  +create(title,author)
  +save(book)
  +delete(id)
}
class InMemoryBookRepository
class DjangoBookRepository
class TitlePolicy {
  <<abstract>>
  +normalize(title)
}
class KeepCaseTitlePolicy
class CompactWhitespaceTitlePolicy

BookService --> BookRepository : client–supplier
BookService --> TitlePolicy : uses
BookRepository <|-- InMemoryBookRepository
BookRepository <|-- DjangoBookRepository
TitlePolicy <|-- KeepCaseTitlePolicy
TitlePolicy <|-- CompactWhitespaceTitlePolicy
BookRepository --> Book : works with
~~~

Diagram di atas menyederhanakan detail aplikasi Django.
Dalam implementasi, `DjangoBookRepository` hidup di proyek Django,
dan menjembatani `books.models.Book` (ORM row) ke `book_domain.Book`
(domain entity); lihat [ARCHITECTURE_COMPARISON.md](ARCHITECTURE_COMPARISON.md).

**Has-a vs is-a:** `BookService` **menggunakan** repository dan policy
(has-a, composition). `InMemoryBookRepository` **adalah salah satu jenis**
`BookRepository` (is-a, inheritance). Jangan menulis
`class BookService(BookRepository)`: service bukan jenis repository.

## Tahap 3 — Mengimplementasikan OOP tanpa web (OOP)

Ikuti file sesuai urutan:

1. [entities.py](00-pure-python/src/book_domain/entities.py):
   `Book.__init__`, `validated_fields`, `revise`, `id`.
2. [ports.py](00-pure-python/src/book_domain/ports.py):
   kontrak abstract `BookRepository`.
3. [memory.py](00-pure-python/src/book_domain/memory.py):
   subclass yang implement operasi menggunakan dictionary.
4. [policies.py](00-pure-python/src/book_domain/policies.py):
   variasi perilaku melalui overriding `normalize()`.
5. [services.py](00-pure-python/src/book_domain/services.py):
   `BookService` mengorkestrasi objek-objek lain tanpa HTTP.
6. [test_domain.py](00-pure-python/tests/test_domain.py):
   unit test masing-masing invariant, alias, dan polymorphism.

Contoh nyata:

~~~python
from book_domain import BookService, InMemoryBookRepository

repo = InMemoryBookRepository()
service = BookService(repo)            # composition
book = service.create(" OOP ", " Dosen ")
assert book.title == "OOP"
assert service.get(book.id) is book   # alias/reference pada adapter memory
service.update(book.id, "Design", "Dosen")
assert book.title == "Design"
~~~

Ini mempraktikkan Modul 11: dua referensi Python dapat menunjuk objek
yang sama (bukan berarti dua record database berbeda). Di Django, setiap
query ORM dapat membangun objek Python baru yang mewakili ID logis sama.

## Tahap 4 — Memilih adapter: Flask, FastAPI, atau Django

Ketiga framework mengimpor paket Python yang sama (`book_domain`).
Handler adalah **adapter HTTP**, bukan tempat aturan bisnis baru.

~~~mermaid
flowchart TD
    C[Client JSON Request] --> F{Framework}
    F -->|FastAPI| A[FastAPI Endpoint and Pydantic]
    F -->|Flask| B[Flask Route and JSON Parser]
    F -->|Django| D[Django URL and View]
    A --> S[BookService]
    B --> S
    D --> S
    S --> E[Book and TitlePolicy]
    S --> R[BookRepository ABC]
    R --> M[InMemoryBookRepository]
    R --> O[DjangoBookRepository]
    O --> DB[(Django ORM / SQLite)]
~~~

*Penting:* diagram menggabungkan tiga pilihan aplikasi. Pada saat menjalankan
satu server, hanya satu rute framework dan satu repository yang dipakai;
bukan ketiga server memproses request yang sama secara bersamaan.

### Siklus POST /books (contoh)

1. Client mengirim JSON `{"title":"Clean Code","author":"Robert C. Martin"}`.
2. Framework mencocokkan route dan mengurai input.
3. Handler memanggil `BookService.create(title, author)`.
4. Service memakai `TitlePolicy`, kemudian memeriksa invariant `Book`.
5. Service meminta repository membuat `Book` dan mengembalikan objek domain.
6. Handler mengubah `Book.to_dict()` menjadi JSON dan HTTP **201**.

**HTTP concerns** = routing, body/JSON, status code, request validation.
**Domain concerns** = invariant, valid state transition, repository abstraction.
**Persistence concerns** = penyimpanan dict/ORM. Memisahkan ini membuat
tanggung jawab tiap bagian lebih mudah diubah dan diuji.

### Kaitan exception (Modul 13)

- `BookValidationError` adalah kegagalan kontrak domain.
  FastAPI mengembalikan **422**; Flask/Django mengembalikan **400**.
- `BookNotFound` menjadi respons **404**.
- Perbedaan kode status berada di adapter HTTP; **domain tidak berubah**.

## Tahap 5 — Pengujian (OOT) dari dalam ke luar

| Level | Tes | Perlu HTTP? | Perlu database? |
|---|---|---|---|
| Domain | `test_domain.py` | Tidak | Tidak |
| Adapter FastAPI | `fastapi/tests/test_api.py` | TestClient, tanpa network | Tidak |
| Adapter Flask | `flask/tests/test_api.py` | test_client, tanpa network | Tidak |
| Django integration | `django/books/tests.py` dan test adapter | test client, tanpa network | Ya, test SQLite sementara |

Mulailah dari invariant domain, bukan hanya status sukses HTTP.
Misalnya: jika judul baru valid tetapi pengarang kosong, **judul tidak
boleh ikut berubah**. Tes ini memvalidasi desain objek, bukan framework.

## Tahap 6 — Refleksi desain (Modul 15)

Bandingkan tiga keputusan:

- **Abstraction:** port repository memungkinkan implementasi in-memory dan ORM
  dapat saling menggantikan pada `BookService`.
- **Polymorphism:** service memanggil kontrak yang sama; method konkret
  dipilih berdasarkan runtime type repository/policy.
- **Strategy-style:** `KeepCaseTitlePolicy` vs
  `CompactWhitespaceTitlePolicy` menunjukkan satu variasi perilaku
  yang jelas. Jika variasi itu tidak dibutuhkan, cukup gunakan policy default.

Jangan menambah inheritance atau pattern sekadar untuk menghitung jumlah
fitur OOP. Tujuannya adalah tanggung jawab yang dapat dijelaskan.

## Jalur praktik yang disarankan

1. Jalankan `00-pure-python/demo.py`, lalu unit test-nya.
2. Pelajari FastAPI: otomatisasi skema HTTP oleh Pydantic.
3. Pelajari Flask: handler/parsing manual dengan service yang sama.
4. Pelajari Django: ORM Book bukan entitas domain Book; repository melakukan mapping.
5. Bandingkan kesamaan method `BookService` dari tiga aplikasi.
6. Kerjakan [latihan bertingkat](exercises/beginner.md) dan
   [panduan fasilitator](INSTRUCTOR_EXTENSION_GUIDE.md).

Tugas ini tidak mengubah bobot atau kriteria penilaian modul inti.
