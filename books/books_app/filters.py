import django_filters
from django_filters import DateFilter, CharFilter
from django.forms.widgets import TextInput, DateInput

from .models import *


class BooksFilter(django_filters.FilterSet):
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
    # start_date = DateFilter(
    #     field_name="publication_date",
    #     lookup_expr="gte",
    #     widget=DateInput(attrs={"placeholder": "YYYY-MM-DD", "style": "max-width:10em", "class": "form-control form-control-sm"})
    # )
    # end_date = DateFilter(
    #     field_name="publication_date",
    #     lookup_expr="lte",
    #     widget=DateInput(attrs={"placeholder": "YYYY-MM-DD", "style": "max-width:10em"})
    # )
    publication_date = django_filters.DateFromToRangeFilter(
        field_name="publication_date",
        widget=django_filters.widgets.RangeWidget(
            attrs={'placeholder': 'YYYY-MM-DD', "style": "max-width:7em"}
        )
    )

    class Meta:
        model = Book
        fields = "__all__"
        exclude = ["isbn", "pages", "link", "publication_date"]


class ImportFilter(django_filters.FilterSet):
    title = CharFilter(field_name="title", lookup_expr="icontains")

