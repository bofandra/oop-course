"""All book endpoints are mounted at /books (without a trailing slash)."""

from django.urls import include, path


urlpatterns = [path("", include("books.urls"))]
