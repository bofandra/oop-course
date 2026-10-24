import json

from django.test import TestCase

from .models import Book


class BookApiTests(TestCase):
    def send_json(self, method, path, payload):
        return getattr(self.client, method)(
            path,
            data=json.dumps(payload),
            content_type="application/json",
        )

    def test_complete_crud(self):
        self.assertEqual(self.client.get("/books").json(), [])
        created = self.send_json(
            "post", "/books", {"title": " Clean Code ", "author": " Robert C. Martin "}
        )
        self.assertEqual(created.status_code, 201)
        self.assertEqual(
            created.json(), {"id": 1, "title": "Clean Code", "author": "Robert C. Martin"}
        )
        self.assertEqual(self.client.get("/books/1").json(), created.json())
        self.assertEqual(Book.objects.count(), 1)

        updated = self.send_json(
            "put", "/books/1", {"title": "Refactoring", "author": "Martin Fowler"}
        )
        self.assertEqual(updated.status_code, 200)
        self.assertEqual(updated.json()["title"], "Refactoring")
        self.assertEqual(self.client.delete("/books/1").status_code, 204)
        self.assertEqual(self.client.get("/books").json(), [])

    def test_input_validation(self):
        for payload in [
            {"title": " ", "author": "Jane"},
            {"title": "Book", "author": ""},
            {"title": 123, "author": "Jane"},
            {"title": "x" * 121, "author": "Jane"},
            {"title": "Only title"},
        ]:
            with self.subTest(payload=payload):
                self.assertEqual(self.send_json("post", "/books", payload).status_code, 400)
        self.assertEqual(
            self.client.post("/books", data="not json", content_type="application/json").status_code,
            400,
        )

    def test_missing_book(self):
        self.assertEqual(self.client.get("/books/9").status_code, 404)
        self.assertEqual(
            self.send_json("put", "/books/9", {"title": "X", "author": "Y"}).status_code,
            404,
        )
        self.assertEqual(self.client.delete("/books/9").status_code, 404)

    def test_method_not_allowed(self):
        self.assertEqual(self.client.post("/books/3").status_code, 405)
