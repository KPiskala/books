from django.test import TestCase, Client
from django.urls import reverse
from books_app.models import Book
from datetime import date


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.books_list_url = reverse("books_app:books_list")
        self.import_books_url = reverse("books_app:import_books")
        self.add_book_url = reverse("books_app:add_book")
        self.test_book = Book.objects.create(
            title="Test title",
            author="Test author",
            publication_date=date(year=2021, month=8, day=1),
            isbn="123454321",
            pages=200,
            link=None,
            language="en"
        )

    def test_books_list_GET(self):
        response = self.client.get(self.books_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "books_app/books_list.html")

    def test_import_books_GET(self):
        response = self.client.get(self.import_books_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "books_app/import_books.html")

    def test_add_book_redirects(self):
        response = self.client.post(self.add_book_url, {
            "title": "Title (Test)",
            "author": "Author (Test)",
            "publication_date": date(year=2020, month=9, day=1),
            "isbn": "0981",
            "pages": 213,
            "link": "https://www.youtube.com",
            "language": "en"
        })
        self.assertEquals(response.status_code, 302)

    def test_add_book_adds_data(self):
        isbn = "0987654321"
        self.client.post(self.add_book_url, {
            "title": "Title (Test)",
            "author": "Author (Test)",
            "publication_date": date(year=2020, month=9, day=1),
            "isbn": isbn,
            "pages": 213,
            "link": "https://www.youtube.com",
            "language": "en"
        })
        assert Book.objects.filter(isbn=isbn).exists()

    def test_edit_book_existing_isbn_redirects(self):
        response = self.client.get(reverse("books_app:edit_book", args=[self.test_book.isbn]))

        self.assertTemplateUsed(response, "books_app/edit_book.html")
        self.assertEquals(response.status_code, 200)

    def test_edit_book_non_existing_isbn_redirects(self):
        non_existing_isbn = "1111111112222211"
        response = self.client.get(reverse("books_app:edit_book", args=[non_existing_isbn]))

        self.assertEquals(response.status_code, 404)

    def test_edit_book_edits_data(self):
        self.client.post(
            reverse("books_app:edit_book", args=[self.test_book.isbn]),
            {
                "title": "Changed test title",
                "author": "Changed test author",
                "publication_date": date(year=2021, month=3, day=15),
                "pages": 500,
                "link": "https://www.google.com",
                "language": "pl"
            }
        )
        changed_object = Book.objects.get(
            title="Changed test title",
            author="Changed test author",
            publication_date=date(year=2021, month=3, day=15),
            isbn="123454321",
            pages=500,
            link="https://www.google.com",
            language="pl"
        )
        self.assertEqual(changed_object, self.test_book)
