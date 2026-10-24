import unittest

from book_domain import InMemoryBookRepository

from app import create_app


class BookApiTests(unittest.TestCase):
    def setUp(self):
        self.client = create_app(InMemoryBookRepository()).test_client()

    def test_complete_crud(self):
        self.assertEqual(self.client.get("/books").json, [])
        created = self.client.post(
            "/books", json={"title": " Clean Code ", "author": " Robert C. Martin "}
        )
        self.assertEqual(created.status_code, 201)
        self.assertEqual(
            created.json, {"id": 1, "title": "Clean Code", "author": "Robert C. Martin"}
        )
        self.assertEqual(self.client.get("/books/1").json, created.json)
        self.assertEqual(len(self.client.get("/books").json), 1)
        updated = self.client.put(
            "/books/1", json={"title": "Refactoring", "author": "Martin Fowler"}
        )
        self.assertEqual(updated.status_code, 200)
        self.assertEqual(updated.json["title"], "Refactoring")
        self.assertEqual(self.client.delete("/books/1").status_code, 204)
        self.assertEqual(self.client.get("/books").json, [])

    def test_input_validation(self):
        for payload in [
            {"title": " ", "author": "Jane"},
            {"title": "Book", "author": ""},
            {"title": 123, "author": "Jane"},
            {"title": "x" * 121, "author": "Jane"},
            {"title": "Only title"},
        ]:
            with self.subTest(payload=payload):
                self.assertEqual(self.client.post("/books", json=payload).status_code, 400)
        self.assertEqual(
            self.client.post("/books", data="not json", content_type="application/json").status_code,
            400,
        )

    def test_missing_book(self):
        self.assertEqual(self.client.get("/books/9").status_code, 404)
        self.assertEqual(
            self.client.put("/books/9", json={"title": "X", "author": "Y"}).status_code, 404
        )
        self.assertEqual(self.client.delete("/books/9").status_code, 404)

    def test_invalid_update_does_not_change_existing_book(self):
        self.client.post("/books", json={"title": "Original", "author": "Teacher"})
        invalid = self.client.put("/books/1", json={"title": "Changed", "author": " "})
        self.assertEqual(invalid.status_code, 400)
        self.assertEqual(self.client.get("/books/1").json["title"], "Original")


if __name__ == "__main__":
    unittest.main()
