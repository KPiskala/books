import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class BooksFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="publication_date", lookup_expr="gte")
    end_date = DateFilter(field_name="publication_date", lookup_expr="lte")
    title = CharFilter(field_name="title", lookup_expr="icontains")
    author = CharFilter(field_name="author", lookup_expr="icontains")

    class Meta:
        model = Book
        fields = "__all__"
        exclude = ["isbn", "pages", "link", "publication_date"]


class ImportFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr="icontains")

