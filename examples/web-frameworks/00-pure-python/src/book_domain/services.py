"""Application service coordinates collaborators and business operations."""

from .entities import Book
from .errors import BookNotFound
from .policies import KeepCaseTitlePolicy, TitlePolicy
from .ports import BookRepository


class BookService:
    """Composition: repository and policy are provided by the caller."""

    def __init__(
        self,
        repository: BookRepository,
        title_policy: TitlePolicy | None = None,
    ) -> None:
        self._repository = repository
        self._title_policy = (
            title_policy if title_policy is not None else KeepCaseTitlePolicy()
        )

    def list(self) -> list[Book]:
        return self._repository.list()

    def get(self, book_id: int) -> Book:
        book = self._repository.get(book_id)
        if book is None:
            raise BookNotFound(f"Book {book_id} not found")
        return book

    def create(self, title: str, author: str) -> Book:
        normalized = self._title_policy.normalize(title)
        clean_title, clean_author = Book.validated_fields(normalized, author)
        return self._repository.create(clean_title, clean_author)

    def update(self, book_id: int, title: str, author: str) -> Book:
        book = self.get(book_id)
        normalized = self._title_policy.normalize(title)
        book.revise(normalized, author)
        self._repository.save(book)
        return book

    def delete(self, book_id: int) -> None:
        if not self._repository.delete(book_id):
            raise BookNotFound(f"Book {book_id} not found")
