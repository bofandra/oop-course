"""Concrete adapter for the repository interface: process-local dict."""

from .entities import Book
from .errors import BookNotFound
from .ports import BookRepository


class InMemoryBookRepository(BookRepository):
    """Simple demo storage. Object references are shared within one process."""

    def __init__(self) -> None:
        self._books: dict[int, Book] = {}
        self._next_id = 1

    def list(self) -> list[Book]:
        return [self._books[k] for k in sorted(self._books)]

    def get(self, book_id: int) -> Book | None:
        return self._books.get(book_id)

    def create(self, title: str, author: str) -> Book:
        # Book validates input before the repository updates its own state.
        book = Book(self._next_id, title, author)
        self._books[book.id] = book
        self._next_id += 1
        return book

    def save(self, book: Book) -> None:
        if book.id not in self._books:
            raise BookNotFound(f"Book {book.id} not found")
        self._books[book.id] = book

    def delete(self, book_id: int) -> bool:
        return self._books.pop(book_id, None) is not None
