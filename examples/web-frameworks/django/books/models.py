"""Django's persistence model, deliberately separate from domain Book.

The ORM model inherits models.Model; BookRepository maps rows to domain Book.
This is a deliberate architectural trade-off, not a Django requirement.
"""

from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.title} — {self.author}"
