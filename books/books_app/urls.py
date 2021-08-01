from django.urls import path
from .views import add_book, edit_book, books_list, import_books

app_name = "books_app"
urlpatterns = [
    path('add_book/', add_book, name="add_book"),
    path('edit_book/<int:id>/', edit_book, name="edit_book"),
    path('books_list/', books_list, name="books_list"),
    path('import_books/', import_books, name="import_books"),
]
