"""FastAPI is an HTTP adapter; OOP behavior lives in book_domain.

Read: 00-pure-python/src/book_domain, then this file.
Relevant OOP modules: 4, 5, 9, 13, 14, 15.
"""

from typing import Annotated

from book_domain import (
    BookNotFound,
    BookRepository,
    BookService,
    BookValidationError,
    InMemoryBookRepository,
)
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, StringConstraints


NonEmptyText = Annotated[
    str, StringConstraints(strip_whitespace=True, min_length=1, max_length=120)
]


class BookInput(BaseModel):
    """HTTP input schema; not the domain Book entity."""
    title: NonEmptyText
    author: NonEmptyText


class BookOutput(BookInput):
    id: int


def create_app(repository: BookRepository | None = None) -> FastAPI:
    """Composition root: wire a repository to a domain service."""
    storage = repository if repository is not None else InMemoryBookRepository()
    service = BookService(storage)
    app = FastAPI(title="Book API - FastAPI", version="2.0.0")

    @app.get("/books", response_model=list[BookOutput])
    def list_books() -> list[dict]:
        return [book.to_dict() for book in service.list()]

    @app.get("/books/{book_id}", response_model=BookOutput)
    def get_book(book_id: int) -> dict:
        try:
            return service.get(book_id).to_dict()
        except BookNotFound as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc

    @app.post("/books", response_model=BookOutput, status_code=201)
    def create_book(data: BookInput) -> dict:
        # Pydantic validates the HTTP body; domain independently enforces invariants.
        try:
            return service.create(data.title, data.author).to_dict()
        except BookValidationError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    @app.put("/books/{book_id}", response_model=BookOutput)
    def update_book(book_id: int, data: BookInput) -> dict:
        try:
            return service.update(book_id, data.title, data.author).to_dict()
        except BookNotFound as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        except BookValidationError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    @app.delete("/books/{book_id}", status_code=204)
    def delete_book(book_id: int) -> Response:
        try:
            service.delete(book_id)
        except BookNotFound as exc:
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        return Response(status_code=204)

    return app


app = create_app()
