# Django — ORM adapter untuk domain Book yang sama

> Baca [00-pure-python](../00-pure-python/README.md),
> [learning bridge](../OOP_LEARNING_BRIDGE.md), dan
> [architecture comparison](../ARCHITECTURE_COMPARISON.md).

## Poin OOP yang wajib dipahami dalam studi kasus ini

Ada **dua class Book yang berbeda tanggung jawabnya**:

1. `book_domain.Book` — domain entity dengan invariant,
   encapsulation dan behavior `revise()`.
2. `books.models.Book(models.Model)` — class **ORM** sebagai mapping
   kolom `title`, `author`, dan primary key pada SQLite.

`DjangoBookRepository(BookRepository)` adalah adapter yang
memetakan ORM Book ke domain Book melalui `_to_domain()`. Karena
adapter ini memenuhi abstract contract yang sama dengan
`InMemoryBookRepository`, **BookService tidak diubah**.

~~~mermaid
classDiagram
class BookService
class BookRepository {
  <<abstract>>
  +get(id)
  +create(title,author)
  +save(book)
}
class DjangoBookRepository {
  +get(id)
  +create(title,author)
  +save(book)
}
class DomainBook {
  +revise(title,author)
  +to_dict()
}
class DjangoORMBook {
  +title
  +author
  +save()
}
BookService --> BookRepository : uses
BookRepository <|-- DjangoBookRepository
DjangoBookRepository --> DjangoORMBook : reads/writes
DjangoBookRepository --> DomainBook : maps into
~~~

Ini merupakan **pilihan desain untuk mengajar OOP lintas framework**,
bukan aturan bahwa Django wajib memiliki dua model.
Aplikasi sederhana boleh menggunakan rich Django ORM model langsung.

## Alur request

~~~text
Django config/urls.py -> books/urls.py -> books/views.py
    -> service_for_request() -> BookService(DjangoBookRepository())
    -> domain Book (validasi)
    -> DjangoBookRepository -> ORM Book -> SQLite
    -> domain Book -> .to_dict() -> JsonResponse
~~~

Modul yang relevan: 5 (has-a), 6–7 (is-a/overriding), 9 (ABC),
11 (ID logis vs object identity hasil ORM), 12–13 (modules/exceptions),
14–15 (desain + tests).

## Menjalankan (Python 3.12+)

~~~bash
cd examples/web-frameworks/django
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8003
~~~

~~~bash
curl -i -X POST http://127.0.0.1:8003/books \
  -H "Content-Type: application/json" \
  -d '{"title":"Clean Code","author":"Robert C. Martin"}'
python manage.py test books -v 2
python manage.py makemigrations --check --dry-run
~~~

Test runner Django menggunakan database test tersendiri;
jangan arahkan ke database produksi.

## Diskusi/refleksi

1. Apa beda inheritance `Book(models.Model)` dengan composition
   `BookService(DjangoBookRepository())`?
2. Dua `Book` dengan ID 1 yang dibuat dari dua ORM query berbeda
   bisa mewakili record sama, tetapi apakah selalu `is` sama?
3. Mengapa `DjangoBookRepository` adalah lokasi tepat untuk
   menerjemahkan record ke domain object?
4. Jika mengganti SQLite menjadi database lain melalui Django ORM,
   perubahan apa yang diperlukan di domain?
5. Apa trade-off membuat domain class + ORM class dibanding satu
   rich Django model?

## Batasan

Contoh menggunakan JSON views Django native **tanpa DRF** agar
hubungan antarobjek terlihat. Konfigurasi `DEBUG=True`,
`SECRET_KEY` development, SQLite dan `csrf_exempt` hanya untuk
local demo unauthenticated API. Jangan memakai pola ini pada aplikasi
berbasis session/cookie dan jangan deploy ke produksi apa adanya.
