"""Show that Django ORM implements the same pure-python repository contract."""

from book_domain import Book, BookRepository, BookService, BookValidationError
from django.test import TestCase

from .models import Book as BookRecord
from .repositories import DjangoBookRepository


class RepositoryAdapterTests(TestCase):
    def test_repository_polymorphism_persists_between_service_instances(self):
        adapter = DjangoBookRepository()
        self.assertIsInstance(adapter, BookRepository)
        first = BookService(adapter)
        book = first.create(" Clean Code ", " Robert C. Martin ")
        self.assertIsInstance(book, Book)
        self.assertEqual(BookRecord.objects.get(pk=book.id).title, "Clean Code")

        # New service and new ORM query create a NEW Python domain object
        # representing the SAME logical book ID.
        second = BookService(DjangoBookRepository())
        fetched = second.get(book.id)
        self.assertIsNot(fetched, book)
        self.assertEqual(fetched.id, book.id)
        self.assertEqual(fetched.to_dict(), book.to_dict())

        updated = second.update(book.id, " New Edition ", " Another Author ")
        self.assertEqual(BookRecord.objects.get(pk=book.id).title, "New Edition")
        self.assertEqual(updated.title, "New Edition")

    def test_invalid_edit_does_not_persist(self):
        service = BookService(DjangoBookRepository())
        original = service.create("Original", "Author")
        with self.assertRaises(BookValidationError):
            service.update(original.id, "Changed", " ")
        stored = BookRecord.objects.get(pk=original.id)
        self.assertEqual(stored.title, "Original")
        self.assertEqual(stored.author, "Author")
