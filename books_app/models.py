from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.TextField(max_length=400)
    author = models.TextField(max_length=400)
    publication_date = models.DateField()
    isbn = models.TextField(max_length=20, primary_key=True)
    pages = models.IntegerField(null=True)
    link = models.TextField(max_length=400, null=True)
    language = models.TextField(max_length=100, null=True)
