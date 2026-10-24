"""Entity: identity, state, behavior, and invariant in one object."""

from .errors import BookValidationError


class Book:
    """Logical identity is id, independent of Python's object identity."""

    def __init__(self, book_id: int, title: str, author: str) -> None:
        if type(book_id) is not int or book_id < 1:
            raise BookValidationError("id must be a positive integer")
        clean_title, clean_author = self.validated_fields(title, author)
        self._id = book_id
        self._title = clean_title
        self._author = clean_author

    @staticmethod
    def _clean(field: str, value: str) -> str:
        if not isinstance(value, str):
            raise BookValidationError(f"{field} must be a string")
        clean = value.strip()
        if not 1 <= len(clean) <= 120:
            raise BookValidationError(f"{field} must contain 1-120 characters")
        return clean

    @classmethod
    def validated_fields(cls, title: str, author: str) -> tuple[str, str]:
        """Validate both values BEFORE modifying any state."""
        return cls._clean("title", title), cls._clean("author", author)

    @property
    def id(self) -> int:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    def revise(self, title: str, author: str) -> None:
        """Atomic at object level: invalid author cannot half-update title."""
        new_title, new_author = self.validated_fields(title, author)
        self._title, self._author = new_title, new_author

    def rename(self, new_title: str) -> None:
        self.revise(new_title, self._author)

    def to_dict(self) -> dict[str, str | int]:
        """Serialization boundary; callers never need private attributes."""
        return {"id": self.id, "title": self.title, "author": self.author}
