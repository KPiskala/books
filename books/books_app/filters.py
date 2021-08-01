from django_filters import FilterSet, DateFromToRangeFilter, CharFilter, widgets
from django.forms.widgets import TextInput

from .models import *


class BooksFilter(FilterSet):
    title = CharFilter(
        field_name="title",
        lookup_expr="icontains",
        widget=TextInput(attrs={"style": "max-width:10em"})
    )
    author = CharFilter(
        field_name="author",
        lookup_expr="icontains",
        widget=TextInput(attrs={"style": "max-width:10em"})
    )
    language = CharFilter(
        field_name="language",
        widget=TextInput(attrs={"style": "max-width:10em"})
    )
    publication_date = DateFromToRangeFilter(
        field_name="publication_date",
        widget=widgets.RangeWidget(
            attrs={"placeholder": "YYYY-MM-DD", "style": "max-width:7em"}
        )
    )

    class Meta:
        model = Book
        fields = "__all__"
        exclude = ["isbn", "pages", "link", "publication_date"]


class ImportFilter(FilterSet):
    title = CharFilter(field_name="title", lookup_expr="icontains")
