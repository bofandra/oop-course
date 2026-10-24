"""Small Strategy demonstration: interchangeable title normalization."""

from abc import ABC, abstractmethod

from .errors import BookValidationError


class TitlePolicy(ABC):
    @abstractmethod
    def normalize(self, title: str) -> str:
        raise NotImplementedError


class KeepCaseTitlePolicy(TitlePolicy):
    def normalize(self, title: str) -> str:
        if not isinstance(title, str):
            raise BookValidationError("title must be a string")
        return title.strip()


class CompactWhitespaceTitlePolicy(TitlePolicy):
    """Optional example variation, not a mandatory policy for all books."""

    def normalize(self, title: str) -> str:
        if not isinstance(title, str):
            raise BookValidationError("title must be a string")
        return " ".join(title.split())
