# Perbandingan arsitektur: domain yang sama, tiga adapter HTTP

## Batas dependensi

~~~text
          REQUEST                     DOMAIN                       STORAGE
FastAPI ── Pydantic ──┐
Flask ──── JSON ──────┼──────> BookService ────────> BookRepository ABC
Django ─── JSON ──────┘            |                      /      \
                              Book, TitlePolicy        dict    Django ORM
                                   |                               |
                           Invariants & behavior                SQLite
~~~

Paket `book_domain` tidak mengimpor framework, ORM, atau HTTP library.
Ketiga proyek memasang paket ini melalui `-e ../00-pure-python`.
Masing-masing HTTP adapter memanggil `BookService` yang sama.

## Sequence POST /books di Django

~~~mermaid
sequenceDiagram
    autonumber
    participant C as HTTP Client
    participant V as Django View
    participant S as BookService
    participant P as TitlePolicy
    participant D as Book (domain)
    participant R as DjangoBookRepository
    participant DB as ORM / SQLite
    C->>V: POST /books + JSON
    V->>S: create(title,author)
    S->>P: normalize(title)
    P-->>S: normalized title
    S->>D: validated_fields(title,author)
    D-->>S: clean fields
    S->>R: create(title,author)
    R->>DB: INSERT books_book
    DB-->>R: ORM record (id)
    R->>D: Book(id,title,author)
    D-->>R: domain object
    R-->>S: Book
    S-->>V: Book
    V-->>C: JSON + 201
~~~

Pada FastAPI/Flask, urutannya sama tetapi implementasi repository adalah
`InMemoryBookRepository`; tidak ada ORM maupun SQLite.

## Dua class berbeda bernama Book pada Django

- `book_domain.Book` = domain entity. Menegakkan invariant dan menyediakan behavior.
- `books.models.Book(models.Model)` = ORM mapping satu baris database.
- `DjangoBookRepository._to_domain` = menerjemahkan ORM record ke domain object.

Ini **keputusan contoh**, bukan persyaratan Django. Aplikasi Django kecil
dapat memakai rich Django Model sendiri tanpa domain terpisah. Di sini
pemisahan disengaja agar desain OOP dapat diterapkan ulang lintas framework.

## Perbandingan tanggung jawab

| Bagian | Pure Python | FastAPI | Flask | Django |
|---|---|---|---|---|
| Aturan judul/pengarang | `Book` | Memakai `Book` yang sama | Sama | Sama |
| Use case | `BookService` | Memakai service | Sama | Sama |
| Polymorphic contract | `BookRepository` | InMemory implementasi | InMemory implementasi | ORM implementasi |
| Input HTTP | Tidak ada | Pydantic `BookInput` | `parse_json_body` | `parse_book_input` |
| HTTP errors | Tidak ada | 422 / 404 | 400 / 404 | 400 / 404 |
| Output HTTP | `Book.to_dict()` (bukan HTTP) | FastAPI serializes | `jsonify` | `JsonResponse` |
| Persistence | In-memory demo | In-memory demo | In-memory demo | SQLite |
| Identity across reads | Referensi Book sama | Selama app/repository sama | Selama app/repository sama | Domain Book instance baru dari ORM query |

### Dua lapis validasi bukan duplikasi aturan bisnis

FastAPI/Pydantic memvalidasi bentuk request untuk antarmuka HTTP.
Domain `Book.validated_fields()` memvalidasi invariant **bahkan saat
service dipanggil bukan dari HTTP** (misalnya CLI atau job). Flask/Django
contoh ini membatasi handler pada parsing JSON dan menyerahkan validasi
nilai ke domain.

Karena itu Pydantic `BookInput` **bukan subclass** dari domain `Book`.
Mereka memiliki responsibility berbeda.

### Dampak perubahan kebutuhan (change-impact test)

| Perubahan | Di mana mengubah kode? | Di mana tidak perlu berubah? |
|---|---|---|
| Minimum panjang judul menjadi 3 | `Book` domain + test; sinkronkan schema FastAPI | repository implementasi |
| Mengganti SQLite dengan PostgreSQL Django | konfigurasi DB/ops, jika ORM tetap sama | `BookService`, HTTP contract |
| Menambah field year | entity, repository adapters + migration, schemas, tests | prinsip ABC/Strategy |
| Mengganti FastAPI menjadi Flask | HTTP adapter & setup | `BookService`, domain rules |
| Variasi whitespace title | TitlePolicy pilihan | ORM schema dan handler |

### Risiko dan trade-off (untuk pembelajaran desain)

- In-memory repository berbagi reference dan tidak safe untuk multi-process.
  Contoh cocok mempelajari alias/lifecycle (Modul 11), bukan produksi.
- Django ORM mempersist data, tetapi contoh ini belum mengatur transaction
  untuk write bersamaan; object-level atomic `revise()` **bukan**
  transaksi database.
- Abstraksi tambahan menambah file dan indirection. Aplikasi kecil mungkin
  cukup memakai model ORM langsung, tanpa repository port. Penggunaannya
  di sini disengaja demi transparansi OOP lintas framework.
- Endpoint sengaja tanpa autentikasi, CSRF untuk cookie sessions,
  pagination, auditing, atau observability produksi.

## Pertanyaan akhir

**Mana perubahan yang muncul karena framework, dan mana yang muncul
karena desain domain?** Jelaskan melalui dependency arrows dan nama class.
