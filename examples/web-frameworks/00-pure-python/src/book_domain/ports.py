"""Abstraction: the service needs capabilities, not a database vendor."""

from abc import ABC, abstractmethod

from .entities import Book


class BookRepository(ABC):
    """Subclasses must implement the same persistence contract."""

    @abstractmethod
    def list(self) -> list[Book]:
        raise NotImplementedError

    @abstractmethod
    def get(self, book_id: int) -> Book | None:
        raise NotImplementedError

    @abstractmethod
    def create(self, title: str, author: str) -> Book:
        raise NotImplementedError

    @abstractmethod
    def save(self, book: Book) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, book_id: int) -> bool:
        raise NotImplementedError
