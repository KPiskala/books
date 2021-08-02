from django.test import TestCase
from books_app.filters import BooksFilter, ImportFilter
from books_app.models import Book
from datetime import date
import json


class TestBooksFilter(TestCase):

    def setUp(self):
        self.qs = Book.objects.all()
        self.empty_books_filter = BooksFilter(data={}, queryset=self.qs)
        self.result = self.empty_books_filter.qs
        self.test_book_1 = Book.objects.create(
            title="Test title",
            author="Test",
            publication_date=date(year=2021, month=8, day=1),
            isbn="12345432231",
            pages=200,
            link=None,
            language="english"
        )
        self.test_book_2 = Book.objects.create(
            title="title",
            author="author",
            publication_date=date(year=2017, month=8, day=2),
            isbn="1234453453245431",
            pages=435,
            link=None,
            language="pl"
        )
        self.test_book_3 = Book.objects.create(
            title="Test 3",
            author="Author 3",
            publication_date=date(year=2014, month=9, day=21),
            isbn="1234543543432231",
            pages=None,
            link=None,
            language="en"
        )
        self.test_book_4 = Book.objects.create(
            title="Title 4",
            author="unknown",
            publication_date=date(year=2018, month=10, day=21),
            isbn="123435433432231",
            pages=456,
            link=None,
            language="en"
        )
        self.test_book_5 = Book.objects.create(
            title="Title 5",
            author="some author",
            publication_date=date(year=2014, month=9, day=25),
            isbn="12342332231",
            pages=213,
            link=None,
            language="pl"
        )

    def test_booksfilter_without_data_returns_all_elements(self):
        self.assertEqual(set(self.result), set(self.qs))

    def test_booksfilter_title_is_filtered_properly(self):
        books_filter = BooksFilter(data={"title": "title"}, queryset=self.qs)
        result = books_filter.qs
        expected_result = Book.objects.filter(title__icontains="title")
        self.assertEqual(set(result), set(expected_result))

    def test_booksfilter_author_is_filtered_properly(self):
        books_filter = BooksFilter(data={"author": "aut"}, queryset=self.qs)
        result = books_filter.qs
        expected_result = Book.objects.filter(author__icontains="aut")
        self.assertEqual(set(result), set(expected_result))

    def test_booksfilter_publication_date_is_filtered_properly(self):
        books_filter = BooksFilter(
            data={"publication_date_min": "2017-08-02", "publication_date_max": "2021-08-01"},
            queryset=self.qs
        )
        result = books_filter.qs
        expected_result = Book.objects.filter(publication_date__range=["2017-08-02", "2021-08-01"])
        self.assertEqual(set(result), set(expected_result))

    def test_booksfilter_language_is_filtered_properly(self):
        books_filter = BooksFilter(data={"language": "pl"}, queryset=self.qs)
        result = books_filter.qs
        expected_result = Book.objects.filter(language__iexact="pl")
        self.assertEqual(set(result), set(expected_result))

    def test_booksfilter_title_and_author_are_filtered_properly(self):
        books_filter = BooksFilter(data={"title": "titl", "author": "au"}, queryset=self.qs)
        result = books_filter.qs
        expected_result = Book.objects.filter(
            title__icontains="title",
            author__icontains="au")
        self.assertEqual(set(result), set(expected_result))

    def test_booksfilter_author_and_language_are_filtered_properly(self):
        books_filter = BooksFilter(data={"author": "Au", "language": "en"}, queryset=self.qs)
        result = books_filter.qs
        expected_result = Book.objects.filter(
            author__icontains="Au",
            language__iexact="en"
        )
        self.assertEqual(set(result), set(expected_result))

    def test_booksfilter_publication_date_and_language_are_filtered_properly(self):
        books_filter = BooksFilter(
            data={"publication_date_min": "2015-08-02", "publication_date_max": "2021-08-01", "language": "en"},
            queryset=self.qs
        )
        result = books_filter.qs
        expected_result = Book.objects.filter(
            publication_date__range=["2017-08-02", "2021-08-01"],
            language__iexact="en"
        )
        self.assertEqual(set(result), set(expected_result))

    def test_booksfilter_all_fileds_are_filtered_properly(self):
        books_filter = BooksFilter(
            data={
                "publication_date_min": "2014-08-02",
                "publication_date_max": "2021-08-01",
                "language": "en",
                "author": "auth",
                "title": "titl"
            },
            queryset=self.qs
        )
        result = books_filter.qs
        expected_result = Book.objects.filter(
            publication_date__range=["2014-08-02", "2021-08-01"],
            language__iexact="en",
            author__icontains="auth",
            title__icontains="titl"
        )
        self.assertEqual(set(result), set(expected_result))
