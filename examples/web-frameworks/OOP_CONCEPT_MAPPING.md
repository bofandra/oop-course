# Matriks keterlacakan: Modul OOP 1–16 → kode studi kasus

Gunakan bersama [COURSE_MAP.md](../../COURSE_MAP.md).
Ini **referensi balik**, bukan perubahan CLO, materi wajib, atau rubrik.

| Modul | Konsep yang sudah dipelajari | Di mana tampak pada studi kasus? | Pertanyaan pemeriksaan pemahaman |
|---:|---|---|---|
| [1](../../week-01/) | Thinking in objects | `book_domain/entities.py: Book` | Mengapa "Book" adalah objek/domain entity? |
| [2](../../week-02/) | Class, object, instance | `Book(...)`, `BookService(...)` | Mana class, mana instance? |
| [3](../../week-03/) | State dan behavior | `Book._title`, `Book.revise()` | State apa yang berubah setelah revise? |
| [4](../../week-04/) | Encapsulation dan abstraction | properti `id/title/author`, `validated_fields` | Mengapa caller memakai method, bukan menulis `_title`? |
| [5](../../week-05/) | Client–supplier, object relationship | `BookService` menggunakan `BookRepository` | Relasi has-a, bukan is-a, di mana? |
| [6](../../week-06/) | Inheritance | `InMemoryBookRepository(BookRepository)` | Apakah setiap client harus subclass supplier? |
| [7](../../week-07/) | Overriding, polymorphism, dynamic binding | `DjangoBookRepository.get` vs `InMemoryBookRepository.get` | Method konkret mana yang dijalankan service? |
| [8](../../week-08/) | Mid-course review | kasus CRUD & diagram class | Jelaskan class, behavior, encapsulation, inheritance |
| [9](../../week-09/) | Abstract class | `ports.py: BookRepository(ABC)` | Mengapa abstract repository tidak bisa langsung dibuat? |
| [10](../../week-10/) | Multiple inheritance/mixins | **Tidak diperlukan** oleh kebutuhan studi kasus | Kapan mixin membantu dan mengapa tidak dipaksakan? |
| [11](../../week-11/) | References, identity, lifecycle | `repo.get(id) is book` di in-memory, domain vs ORM object | Bedakan identity Python, ID logis, dan lifecycle request |
| [12](../../week-12/) | Modules, genericity, operator overloading | `book_domain` sebagai paket terpisah; type hints sederhana | Mengapa class dipisah antarmodul? |
| [13](../../week-13/) | Exceptions, contracts, invariant | `BookValidationError`, `BookNotFound`, `Book.revise` | Bagaimana mencegah perubahan parsial? |
| [14](../../week-14/) | OOA → OOD → OOP → OOT | diagram, requirements, `test_domain.py` dan HTTP tests | Bagaimana membuktikan setiap requirement terpenuhi? |
| [15](../../week-15/) | Reuse dan design patterns | repository polymorphism, `TitlePolicy` Strategy-style | Pola mana menyelesaikan masalah riil? |
| [16](../../week-16/) | Final project | ketiga backend sebagai studi pengembangan lanjutan | Apa trade-off pemilihan framework? |

**Catatan kurikulum:** Modul 10 dan aspek genericity/operator overloading
Modul 12 tidak ditambahkan secara artificial hanya untuk mencentang seluruh
konsep. Pemetaan menunjukkan keterhubungan yang benar, termasuk konsep yang
**tidak diperlukan** dalam kasus ini.

## Kode nyata untuk ditelusuri

- [Domain entity dan invariant](00-pure-python/src/book_domain/entities.py)
- [Port / abstract repository](00-pure-python/src/book_domain/ports.py)
- [Concrete memory repository](00-pure-python/src/book_domain/memory.py)
- [Strategy-style normalization](00-pure-python/src/book_domain/policies.py)
- [Application service dengan composition](00-pure-python/src/book_domain/services.py)
- [Unit test OOP](00-pure-python/tests/test_domain.py)
- [FastAPI endpoint adapter](fastapi/app.py)
- [Flask endpoint adapter](flask/app.py)
- [Django ORM adapter](django/books/repositories.py)
- [Django HTTP adapter](django/books/views.py)

## Pertanyaan lisan/viva opsional

1. Mengapa `Book` domain dapat diuji tanpa Django ataupun Flask?
2. Tunjukkan contoh *is-a* dan *has-a* dari kode, bukan definisi saja.
3. Saat menyimpan melalui SQLite, apakah objek domain dan objek ORM
   memiliki identitas Python (`is`) yang sama?
4. Bagaimana menambah repository berbasis PostgreSQL tanpa mengubah service?
5. Mengapa normalisasi `TitlePolicy` opsional dan bukan alasan membuat
   puluhan subclass tanpa kebutuhan?
6. Bagaimana error domain berbeda dari HTTP status?

## Poin fasilitasi

Minta mahasiswa menjawab menggunakan path file, nama class, dan alur
eksekusi. Jawaban "Django adalah OOP karena menggunakan class" belum cukup;
mahasiswa harus mampu menjelaskan responsibility, relasi, dan dampak
perubahan desain.
