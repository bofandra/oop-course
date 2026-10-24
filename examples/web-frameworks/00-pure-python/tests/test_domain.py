"""No web server, framework, or database needed for these unit tests."""

import unittest

from book_domain import (
    Book,
    BookNotFound,
    BookRepository,
    BookService,
    BookValidationError,
    CompactWhitespaceTitlePolicy,
    InMemoryBookRepository,
)


class TrackingRepository(InMemoryBookRepository):
    """Inheritance/overriding: service uses it through the repository interface."""

    def __init__(self):
        super().__init__()
        self.create_count = 0

    def create(self, title, author):
        self.create_count += 1
        return super().create(title, author)


class BookDomainTests(unittest.TestCase):
    def setUp(self):
        self.repo = InMemoryBookRepository()
        self.service = BookService(self.repo)

    def test_create_and_crud(self):
        b = self.service.create(" Clean Code ", " Robert C. Martin ")
        self.assertEqual(b.to_dict(), {
            "id": 1, "title": "Clean Code", "author": "Robert C. Martin"
        })
        self.assertIs(self.repo.get(1), b)
        self.assertEqual(self.service.get(1).id, 1)
        self.assertEqual(len(self.service.list()), 1)
        self.assertEqual(
            self.service.update(1, "Refactoring", "Martin Fowler").title, "Refactoring"
        )
        self.service.delete(1)
        self.assertEqual(self.service.list(), [])
        with self.assertRaises(BookNotFound):
            self.service.get(1)
        with self.assertRaises(BookNotFound):
            self.service.delete(1)

    def test_invariant_prevents_partial_mutation(self):
        b = self.service.create("Original", "Someone")
        with self.assertRaises(BookValidationError):
            self.service.update(b.id, "Changed", " ")
        self.assertEqual(b.title, "Original")
        self.assertEqual(b.author, "Someone")

    def test_invalid_create_does_not_use_an_id(self):
        with self.assertRaises(BookValidationError):
            self.service.create(" ", "Author")
        self.assertEqual(self.service.create("Valid", "Author").id, 1)

    def test_encapsulation_and_read_only_identity(self):
        b = Book(5, "A", "B")
        b.rename(" New ")
        self.assertEqual(b.title, "New")
        with self.assertRaises(AttributeError):
            b.id = 6

    def test_strategy_polymorphism(self):
        policy = CompactWhitespaceTitlePolicy()
        service = BookService(InMemoryBookRepository(), policy)
        b = service.create("  Python    OOP  ", "Teacher")
        self.assertEqual(b.title, "Python OOP")

    def test_repository_subtyping_and_abstract_contract(self):
        with self.assertRaises(TypeError):
            BookRepository()
        spy = TrackingRepository()
        service = BookService(spy)
        service.create("Book", "Author")
        self.assertEqual(spy.create_count, 1)

    def test_validation_contract(self):
        for title, author in [
            ("", "Someone"), ("Book", ""), ("x" * 121, "Someone"),
            (123, "Someone"), ("Book", None),
        ]:
            with self.subTest(title=title, author=author):
                with self.assertRaises(BookValidationError):
                    self.service.create(title, author)


if __name__ == "__main__":
    unittest.main()
