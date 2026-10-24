"""Domain exceptions are not HTTP status codes."""


class BookValidationError(ValueError):
    """A book violates a domain invariant."""


class BookNotFound(LookupError):
    """No book with the requested logical ID exists."""
