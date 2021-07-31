from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
def home(request):
    context = {}
    return render(request, "home.html", context)


def manage_books(request):
    return render(request, "manage_books.html", {})
