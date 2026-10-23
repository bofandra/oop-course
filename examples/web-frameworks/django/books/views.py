"""Plain Django JSON views, without Django REST Framework."""

import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Book


def serialize_book(book):
    return {"id": book.pk, "title": book.title, "author": book.author}


def parse_book_input(request):
    """Django without DRF: JSON parsing and validation are explicit."""
    if request.content_type != "application/json":
        return None
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None
    if not isinstance(data, dict):
        return None
    title, author = data.get("title"), data.get("author")
    if not isinstance(title, str) or not isinstance(author, str):
        return None
    title, author = title.strip(), author.strip()
    if not title or not author or len(title) > 120 or len(author) > 120:
        return None
    return title, author


# Teaching-only, unauthenticated JSON API. DO NOT use csrf_exempt for
# session/cookie-authenticated production endpoints.
@csrf_exempt
@require_http_methods(["GET", "POST"])
def books_collection(request):
    if request.method == "GET":
        books = Book.objects.order_by("id")
        return JsonResponse([serialize_book(b) for b in books], safe=False)
    fields = parse_book_input(request)
    if fields is None:
        return JsonResponse(
            {"error": "title and author must be non-empty strings (max 120 chars)"},
            status=400,
        )
    book = Book.objects.create(title=fields[0], author=fields[1])
    return JsonResponse(serialize_book(book), status=201)


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def book_detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)

    if request.method == "GET":
        return JsonResponse(serialize_book(book))

    if request.method == "DELETE":
        book.delete()
        return HttpResponse(status=204)

    fields = parse_book_input(request)
    if fields is None:
        return JsonResponse(
            {"error": "title and author must be non-empty strings (max 120 chars)"},
            status=400,
        )
    book.title, book.author = fields
    book.save(update_fields=["title", "author"])
    return JsonResponse(serialize_book(book))
