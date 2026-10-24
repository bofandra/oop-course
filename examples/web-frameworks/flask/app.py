"""Flask is an HTTP adapter; domain logic is in book_domain.

Read: 00-pure-python/src/book_domain, then this file.
Relevant OOP modules: 4, 5, 9, 13, 14, 15.
"""

from book_domain import (
    BookNotFound,
    BookRepository,
    BookService,
    BookValidationError,
    InMemoryBookRepository,
)
from flask import Flask, jsonify, request


def parse_json_body():
    """Translate HTTP JSON to arguments; leave the invariant to Book."""
    if not request.is_json:
        return None
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return None
    return payload.get("title"), payload.get("author")


def create_app(repository: BookRepository | None = None) -> Flask:
    """Composition root: wire a repository to a domain service."""
    storage = repository if repository is not None else InMemoryBookRepository()
    service = BookService(storage)
    app = Flask(__name__)

    def input_fields_or_error():
        fields = parse_json_body()
        if fields is None:
            return None, (jsonify(error="Expected a JSON object"), 400)
        return fields, None

    @app.get("/books")
    def list_books():
        return jsonify([book.to_dict() for book in service.list()])

    @app.get("/books/<int:book_id>")
    def get_book(book_id):
        try:
            return jsonify(service.get(book_id).to_dict())
        except BookNotFound as exc:
            return jsonify(error=str(exc)), 404

    @app.post("/books")
    def create_book():
        fields, error = input_fields_or_error()
        if error is not None:
            return error
        try:
            return jsonify(service.create(*fields).to_dict()), 201
        except BookValidationError as exc:
            return jsonify(error=str(exc)), 400

    @app.put("/books/<int:book_id>")
    def update_book(book_id):
        fields, error = input_fields_or_error()
        if error is not None:
            return error
        try:
            return jsonify(service.update(book_id, *fields).to_dict())
        except BookNotFound as exc:
            return jsonify(error=str(exc)), 404
        except BookValidationError as exc:
            return jsonify(error=str(exc)), 400

    @app.delete("/books/<int:book_id>")
    def delete_book(book_id):
        try:
            service.delete(book_id)
        except BookNotFound as exc:
            return jsonify(error=str(exc)), 404
        return "", 204

    return app


app = create_app()
