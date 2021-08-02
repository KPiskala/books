from django.test import TestCase
from books_app.forms import AddBookForm, EditBookForm
from books_app.models import Book
from datetime import date


class TestAddBookForm(TestCase):

    def setUp(self):
        self.empty_form = AddBookForm({})
        self.valid_form = AddBookForm({
            "title": "AddBookForm Title",
            "author": "AddBookForm Author",
            "publication_date": date(year=2000, month=4, day=14),
            "isbn": "00044400033333002",
            "pages": 285,
            "link": "https://getbootstrap.com/docs/5.0/forms/overview/",
            "language": "en"
        })
        self.test_book = Book.objects.create(
            title="Test title",
            author="Test author",
            publication_date=date(year=2021, month=8, day=1),
            isbn="12345432231",
            pages=200,
            link=None,
            language="en"
        )

    def test_addbookform_with_valid_data_is_valid(self):
        self.assertTrue(self.valid_form.is_valid())

    def test_addbookform_with_no_data_is_not_valid(self):
        self.assertFalse(self.empty_form.is_valid())

    def test_addbookform_title_is_required(self):
        self.assertTrue(self.empty_form.fields["title"].required)

    def test_addbookform_author_is_required(self):
        self.assertTrue(self.empty_form.fields["author"].required)

    def test_addbookform_publication_date_is_required(self):
        self.assertTrue(self.empty_form.fields["publication_date"].required)

    def test_addbookform_isbn_is_required(self):
        self.assertTrue(self.empty_form.fields["isbn"].required)

    def test_addbookform_pages_are_not_required(self):
        self.assertFalse(self.empty_form.fields["pages"].required)

    def test_addbookform_link_is_not_required(self):
        self.assertFalse(self.empty_form.fields["link"].required)

    def test_addbookform_language_is_not_required(self):
        self.assertFalse(self.empty_form.fields["language"].required)

    def test_addbookform_isbn_with_unwanted_characters_is_invalid(self):
        form = AddBookForm({
            "title": "AddBookForm Title",
            "author": "AddBookForm Author",
            "publication_date": date(year=2000, month=4, day=14),
            "isbn": "000-023435-330-02",
            "pages": 285,
            "link": "https://getbootstrap.com/docs/5.0/forms/overview/",
            "language": "en"
        })
        self.assertFalse(form.is_valid())

    def test_addbookform_duplicated_isbn_is_invalid(self):
        form = AddBookForm({
            "title": "AddBookForm Title",
            "author": "AddBookForm Author",
            "publication_date": date(year=2000, month=4, day=14),
            "isbn": self.test_book.isbn,
            "pages": 285,
            "link": "https://getbootstrap.com/docs/5.0/forms/overview/",
            "language": "en"
        })
        self.assertFalse(form.is_valid())

    def test_addbookform_negative_pages_are_invalid(self):
        form = AddBookForm({
            "title": "AddBookForm Title",
            "author": "AddBookForm Author",
            "publication_date": date(year=2000, month=4, day=14),
            "isbn": "467534687634534",
            "pages": -1,
            "link": "https://getbootstrap.com/docs/5.0/forms/overview/",
            "language": "en"
        })
        self.assertFalse(form.is_valid())

    def test_addbookform_zero_pages_are_invalid(self):
        form = AddBookForm({
            "title": "AddBookForm Title",
            "author": "AddBookForm Author",
            "publication_date": date(year=2000, month=4, day=14),
            "isbn": "467534687634534",
            "pages": 0,
            "link": "https://getbootstrap.com/docs/5.0/forms/overview/",
            "language": "en"
        })
        self.assertFalse(form.is_valid())


class TestEditBookForm(TestCase):

    def setUp(self):
        self.empty_form = EditBookForm({})

    def test_editbookform_with_valid_data_is_valid(self):
        form = EditBookForm({
            "title": "AddBookForm Title",
            "author": "AddBookForm Author",
            "publication_date": date(year=2000, month=4, day=14),
            "pages": 285,
            "link": "https://getbootstrap.com/docs/5.0/forms/overview/",
            "language": "en"
        })

        self.assertTrue(form.is_valid())

    def test_editbookform_with_no_data_is_not_valid(self):
        self.assertFalse(self.empty_form.is_valid())

    def test_editbookform_title_is_required(self):
        self.assertTrue(self.empty_form.fields["title"].required)

    def test_editbookform_author_is_required(self):
        self.assertTrue(self.empty_form.fields["author"].required)

    def test_editbookform_publication_date_is_required(self):
        self.assertTrue(self.empty_form.fields["publication_date"].required)

    def test_editbookform_pages_are_not_required(self):
        self.assertFalse(self.empty_form.fields["pages"].required)

    def test_editbookform_link_is_not_required(self):
        self.assertFalse(self.empty_form.fields["link"].required)

    def test_editbookform_language_is_not_required(self):
        self.assertFalse(self.empty_form.fields["language"].required)

    def test_editbookform_negative_pages_are_invalid(self):
        form = EditBookForm({
            "title": "EditBookForm Title",
            "author": "EditBookForm Author",
            "publication_date": date(year=2000, month=4, day=14),
            "pages": -1,
            "link": "https://getbootstrap.com/docs/5.0/forms/overview/",
            "language": "en"
        })
        self.assertFalse(form.is_valid())

    def test_editbookform_zero_pages_are_invalid(self):
        form = EditBookForm({
            "title": "EditBookForm Title",
            "author": "EditBookForm Author",
            "publication_date": date(year=2000, month=4, day=14),
            "pages": 0,
            "link": "https://getbootstrap.com/docs/5.0/forms/overview/",
            "language": "en"
        })
        self.assertFalse(form.is_valid())
