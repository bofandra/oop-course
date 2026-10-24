"""Adapter: map a pure-python Book to Django's ORM Book row.

Relevant OOP modules: 5 (client/supplier), 6 (inheritance),
7 (polymorphism), 9 (abstract class), 14-15 (design/testing/reuse).
"""

from book_domain import Book as DomainBook
from book_domain import BookNotFound, BookRepository

from .models import Book as BookRecord


class DjangoBookRepository(BookRepository):
    """A second concrete repository implementing the same abstract contract."""

    @staticmethod
    def _to_domain(record: BookRecord) -> DomainBook:
        return DomainBook(record.pk, record.title, record.author)

    def list(self) -> list[DomainBook]:
        return [self._to_domain(record) for record in BookRecord.objects.order_by("id")]

    def get(self, book_id: int) -> DomainBook | None:
        record = BookRecord.objects.filter(pk=book_id).first()
        return self._to_domain(record) if record is not None else None

    def create(self, title: str, author: str) -> DomainBook:
        # BookService validates fields before calling create().
        record = BookRecord.objects.create(title=title, author=author)
        return self._to_domain(record)

    def save(self, book: DomainBook) -> None:
        affected = BookRecord.objects.filter(pk=book.id).update(
            title=book.title, author=book.author
        )
        if affected == 0:
            raise BookNotFound(f"Book {book.id} not found")

    def delete(self, book_id: int) -> bool:
        affected, _ = BookRecord.objects.filter(pk=book_id).delete()
        return affected > 0
