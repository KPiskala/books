from django import forms
from datetime import date
from .models import Book


class AddBookForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter the book title.",
                "class": "form-control"
            }
        )
    )
    author = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter the book author.",
                "class": "form-control"
            }
        )
    )
    publication_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Enter the publication date.",
                "class": "form-control"
            }
        ),
        initial=date.min
    )
    isbn = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter the ISBN number.",
                "class": "form-control"
            }
        )
    )
    pages = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Enter the number of pages.",
                "class": "form-control"
            }
        ),
        required=False
    )
    link = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter the link to the book cover.",
                "class": "form-control"
            }
        ),
        required=False
    )
    language = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter the language in which the book is written.",
                "class": "form-control"
            }
        ),
        required=False
    )

    def clean_isbn(self, *args, **kwargs):
        isbn = self.cleaned_data.get("isbn")
        if not all(element.isdigit() for element in isbn):
            raise forms.ValidationError("The ISBN number should consist only of digits.")
        if Book.objects.filter(isbn=isbn).exists():
            raise forms.ValidationError("A book with this ISBN number already exists.")
        return isbn

    def clean_pages(self, *args, **kwargs):
        pages = self.cleaned_data.get("pages")
        if pages is not None and pages <= 0:
            raise forms.ValidationError("The number of pages should be positive.")
        return pages


class EditBookForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter the book title.",
                "class": "form-control"
            }
        )
    )
    author = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter the book author.",
                "class": "form-control"
            }
        )
    )
    publication_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Enter the publication date.",
                "class": "form-control"
            }
        ),
        initial=date.min
    )
    pages = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "placeholder": "Enter the number of pages.",
                "class": "form-control"
            }
        ),
        required=False
    )
    link = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter the link to the book cover.",
                "class": "form-control"
            }
        ),
        required=False
    )
    language = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter the language in which the book is written.",
                "class": "form-control"
            }
        ),
        required=False
    )

    def clean_pages(self, *args, **kwargs):
        pages = self.cleaned_data.get("pages")
        if pages is not None and pages <= 0:
            raise forms.ValidationError("The number of pages should be positive.")
        return pages
