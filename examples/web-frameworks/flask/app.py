"""Flask Book API: explicit HTTP handling + object-oriented repository."""

from dataclasses import asdict, dataclass

from flask import Flask, jsonify, request


@dataclass
class Book:
    id: int
    title: str
    author: str


class BookRepository:
    """State and operations are encapsulated outside HTTP handlers."""

    def __init__(self):
        self._books = {}
        self._next_id = 1

    def list(self):
        return list(self._books.values())

    def get(self, book_id):
        return self._books.get(book_id)

    def create(self, title, author):
        book = Book(id=self._next_id, title=title, author=author)
        self._books[book.id] = book
        self._next_id += 1
        return book

    def update(self, book_id, title, author):
        book = self.get(book_id)
        if book is None:
            return None
        book.title = title
        book.author = author
        return book

    def delete(self, book_id):
        return self._books.pop(book_id, None) is not None


def validate_json_body():
    """Returns validated data or None; contrast with FastAPI/Pydantic."""
    if not request.is_json:
        return None
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return None
    title, author = data.get("title"), data.get("author")
    if not isinstance(title, str) or not isinstance(author, str):
        return None
    title, author = title.strip(), author.strip()
    if not title or not author or len(title) > 120 or len(author) > 120:
        return None
    return title, author


def create_app(repository=None):
    app = Flask(__name__)
    books = repository if repository is not None else BookRepository()

    @app.get("/books")
    def list_books():
        return jsonify([asdict(book) for book in books.list()])

    @app.get("/books/<int:book_id>")
    def get_book(book_id):
        book = books.get(book_id)
        if book is None:
            return jsonify(error="Book not found"), 404
        return jsonify(asdict(book))

    @app.post("/books")
    def create_book():
        fields = validate_json_body()
        if fields is None:
            return jsonify(error="title and author must be non-empty strings (max 120 chars)"), 400
        return jsonify(asdict(books.create(*fields))), 201

    @app.put("/books/<int:book_id>")
    def update_book(book_id):
        fields = validate_json_body()
        if fields is None:
            return jsonify(error="title and author must be non-empty strings (max 120 chars)"), 400
        book = books.update(book_id, *fields)
        if book is None:
            return jsonify(error="Book not found"), 404
        return jsonify(asdict(book))

    @app.delete("/books/<int:book_id>")
    def delete_book(book_id):
        if not books.delete(book_id):
            return jsonify(error="Book not found"), 404
        return "", 204

    return app


app = create_app()
