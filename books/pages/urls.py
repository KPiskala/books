from django.urls import path
from .views import home, manage_books

app_name = "pages"
urlpatterns = [
    path('', home, name='home'),
    path('manage_books/', manage_books, name='manage_books'),
]