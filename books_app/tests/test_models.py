from django.test import TestCase
from books_app.models import Book
from datetime import date


class TestModels(TestCase):

    def setUp(self):
        self.test_book = Book.objects.create(
            title="Test title",
            author="Test author",
            publication_date=date(year=2019, month=3, day=17),
            isbn="45456454454564576",
            pages=200,
            link=None,
            language="en"
        )

    def test_book_is_created_properly(self):
        assert Book.objects.filter(
            title="Test title",
            author="Test author",
            publication_date=date(year=2019, month=3, day=17),
            isbn="45456454454564576",
            pages=200,
            link=None,
            language="en"
        ).exists()
