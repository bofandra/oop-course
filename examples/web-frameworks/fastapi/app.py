"""FastAPI Book API: type-driven validation + explicit repository object."""

from dataclasses import asdict, dataclass
from typing import Annotated

from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, StringConstraints


NonEmptyText = Annotated[
    str, StringConstraints(strip_whitespace=True, min_length=1, max_length=120)
]


class BookInput(BaseModel):
    title: NonEmptyText
    author: NonEmptyText


class BookOutput(BookInput):
    id: int


@dataclass
class Book:
    id: int
    title: str
    author: str


class BookRepository:
    """Encapsulates book state; a demo-only, per-process data store."""

    def __init__(self) -> None:
        self._books: dict[int, Book] = {}
        self._next_id = 1

    def list(self) -> list[Book]:
        return list(self._books.values())

    def get(self, book_id: int) -> Book | None:
        return self._books.get(book_id)

    def create(self, data: BookInput) -> Book:
        book = Book(id=self._next_id, title=data.title, author=data.author)
        self._books[book.id] = book
        self._next_id += 1
        return book

    def update(self, book_id: int, data: BookInput) -> Book | None:
        book = self.get(book_id)
        if book is None:
            return None
        book.title = data.title
        book.author = data.author
        return book

    def delete(self, book_id: int) -> bool:
        return self._books.pop(book_id, None) is not None


def create_app(repository: BookRepository | None = None) -> FastAPI:
    """App factory makes each test use an isolated repository."""
    books = repository if repository is not None else BookRepository()
    app = FastAPI(title="Book API - FastAPI", version="1.0.0")

    def find_or_404(book_id: int) -> Book:
        book = books.get(book_id)
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return book

    @app.get("/books", response_model=list[BookOutput])
    def list_books() -> list[dict]:
        return [asdict(book) for book in books.list()]

    @app.get("/books/{book_id}", response_model=BookOutput)
    def get_book(book_id: int) -> dict:
        return asdict(find_or_404(book_id))

    @app.post("/books", response_model=BookOutput, status_code=201)
    def create_book(data: BookInput) -> dict:
        return asdict(books.create(data))

    @app.put("/books/{book_id}", response_model=BookOutput)
    def update_book(book_id: int, data: BookInput) -> dict:
        book = books.update(book_id, data)
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return asdict(book)

    @app.delete("/books/{book_id}", status_code=204)
    def delete_book(book_id: int) -> Response:
        if not books.delete(book_id):
            raise HTTPException(status_code=404, detail="Book not found")
        return Response(status_code=204)

    return app


app = create_app()
