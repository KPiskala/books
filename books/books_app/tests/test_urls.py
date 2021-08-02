from django.test import SimpleTestCase
from django.urls import reverse, resolve
from books_app.views import *


class TestUrls(SimpleTestCase):

    def test_books_list_url_resolves(self):
        url = reverse("books_app:books_list")
        self.assertEquals(resolve(url).func, books_list)

    def test_add_book_url_resolves(self):
        url = reverse("books_app:add_book")
        self.assertEquals(resolve(url).func, add_book)

    def test_import_books_url_resolves(self):
        url = reverse("books_app:import_books")
        self.assertEquals(resolve(url).func, import_books)

    def test_edit_book_url_resolves(self):
        url = reverse("books_app:edit_book", args=["1"])
        self.assertEquals(resolve(url).func, edit_book)
