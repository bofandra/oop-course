"""Django JSON HTTP adapter; BookService and Book remain framework-independent."""

import json

from book_domain import BookNotFound, BookService, BookValidationError
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .repositories import DjangoBookRepository


def parse_book_input(request):
    """HTTP parsing belongs here; domain validation belongs in Book."""
    if request.content_type != "application/json":
        return None
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None
    if not isinstance(data, dict):
        return None
    return data.get("title"), data.get("author")


def service_for_request():
    """Composition root: use a database adapter behind the same BookRepository ABC."""
    return BookService(DjangoBookRepository())


# Teaching-only, unauthenticated JSON API. DO NOT use csrf_exempt for
# session/cookie-authenticated production endpoints.
@csrf_exempt
@require_http_methods(["GET", "POST"])
def books_collection(request):
    service = service_for_request()
    if request.method == "GET":
        return JsonResponse([b.to_dict() for b in service.list()], safe=False)

    fields = parse_book_input(request)
    if fields is None:
        return JsonResponse({"error": "Expected a JSON object"}, status=400)
    try:
        return JsonResponse(service.create(*fields).to_dict(), status=201)
    except BookValidationError as exc:
        return JsonResponse({"error": str(exc)}, status=400)


@csrf_exempt
@require_http_methods(["GET", "PUT", "DELETE"])
def book_detail(request, book_id):
    service = service_for_request()

    if request.method == "GET":
        try:
            return JsonResponse(service.get(book_id).to_dict())
        except BookNotFound as exc:
            return JsonResponse({"error": str(exc)}, status=404)

    if request.method == "DELETE":
        try:
            service.delete(book_id)
            return HttpResponse(status=204)
        except BookNotFound as exc:
            return JsonResponse({"error": str(exc)}, status=404)

    fields = parse_book_input(request)
    if fields is None:
        return JsonResponse({"error": "Expected a JSON object"}, status=400)
    try:
        return JsonResponse(service.update(book_id, *fields).to_dict())
    except BookNotFound as exc:
        return JsonResponse({"error": str(exc)}, status=404)
    except BookValidationError as exc:
        return JsonResponse({"error": str(exc)}, status=400)
