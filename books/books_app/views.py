from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
import requests
import json
from datetime import date
from .models import Book
from .forms import RawBookForm
from .filters import BooksFilter


# Create your views here.
def add_book(request):
    form = RawBookForm()
    if request.method == "POST":
        form = RawBookForm(request.POST)
        if form.is_valid():
            Book.objects.create(**form.cleaned_data)
            return redirect("books_app:books_list")
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "books_app/add_book.html", context)


def edit_book(request, id):
    selected_book = get_object_or_404(Book, id=id)
    initial_arguments = {
            "title": selected_book.title,
            "author": selected_book.author,
            "publication_date": selected_book.publication_date,
            "isbn": selected_book.isbn,
            "pages": selected_book.pages,
            "link": selected_book.link,
            "language": selected_book.language
        }
    form = RawBookForm(initial=initial_arguments)
    if request.method == "POST":
        form = RawBookForm(
            request.POST,
            initial=initial_arguments
        )
        if form.is_valid():
            Book.objects.filter(id=id).update(**form.cleaned_data)
            return redirect("books_app:books_list")
        else:
            print(form.errors)
    context = {
        "form": form,
        "selected_book": selected_book
    }
    return render(request, "books_app/edit_book.html", context)


def book_details(request):
    book = Book.objects.get(id=1)
    context = {
        'book': book
    }
    return render(request, "books_app/details.html", context)


def import_books(request):
    googleapikey = settings.API_KEY  # TODO remember to provide the key
    params = {
        "q": request.GET.get("q", ""),
        'key': googleapikey,
        'fields': 'items(volumeInfo)'
    }
    google_books = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=params)
    new_books = []
    try:
        books_items = google_books.json()['items']
        for book in books_items:
            new_isbn = ''.join(
                char for char in book['volumeInfo']['industryIdentifiers'][0]['identifier'] if char.isdigit()
            )
            try:
                new_publication_date = date(
                    year=int(book['volumeInfo']['publishedDate'][:4]) if book['volumeInfo']['publishedDate'][:4] else 1,
                    month=int(book['volumeInfo']['publishedDate'][5:7]) if book['volumeInfo']['publishedDate'][
                                                                           5:7] else 1,
                    day=int(book['volumeInfo']['publishedDate'][8:10]) if book['volumeInfo']['publishedDate'][
                                                                          8:10] else 1
                )
            except ValueError:
                new_publication_date = date.min
            Book.objects.get_or_create(
                author=book['volumeInfo']['authors'][0],
                title=book['volumeInfo']['title'],
                publication_date=new_publication_date,
                isbn=new_isbn,
                pages=book['volumeInfo'].get('pageCount', None),
                link=book['volumeInfo'].get('previewLink', None),
                language=book['volumeInfo'].get('language', None),
            )
            new_books.append(Book.objects.filter(isbn=new_isbn).all())
    except KeyError:
        print(google_books)
    context = {
        "new_books": new_books
    }
    return render(request, "books_app/import_books.html", context)


def books_list(request):
    books = Book.objects.all()
    myFilter = BooksFilter(request.GET, queryset=books)
    books = myFilter.qs
    context = {
        "books": books,
        "myFilter": myFilter
    }
    return render(request, "books_app/books_list.html", context)
