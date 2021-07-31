from django import forms
from datetime import date


class RawBookForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter the book title."}
        )
    )
    author = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter the book author."}
        )
    )
    publication_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"placeholder": "Enter the publication date."}
        ),
        initial=date.min
    )
    isbn = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter the ISBN number."}
        )
    )
    pages = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={"placeholder": "Enter the number of pages."}
        ),
        required=False
    )
    link = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter the link to the book cover."}
        ),
        required=False
    )
    language = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Enter the language in which the book is written."}
        ),
        required=False
    )

    def clean_isbn(self, *args, **kwargs):
        isbn = self.cleaned_data.get("isbn")
        if not all(element.isdigit() for element in isbn):
            raise forms.ValidationError("The ISBN number should consist only of digits.")
        return isbn

    def clean_pages(self, *args, **kwargs):
        pages = self.cleaned_data.get("pages")
        if pages is not None and pages <= 0:
            raise forms.ValidationError("The number of pages should be positive.")
        return pages
