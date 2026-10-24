"""Public API of the framework-independent teaching domain."""

from .entities import Book
from .errors import BookNotFound, BookValidationError
from .memory import InMemoryBookRepository
from .policies import CompactWhitespaceTitlePolicy, KeepCaseTitlePolicy, TitlePolicy
from .ports import BookRepository
from .services import BookService

__all__ = [
    "Book",
    "BookNotFound",
    "BookValidationError",
    "BookRepository",
    "BookService",
    "InMemoryBookRepository",
    "TitlePolicy",
    "KeepCaseTitlePolicy",
    "CompactWhitespaceTitlePolicy",
]
