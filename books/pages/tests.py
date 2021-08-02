from django.test import Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import *


class TestUrls(SimpleTestCase):

    def test_home_url_resolves(self):
        url = reverse("pages:home")
        self.assertEquals(resolve(url).func, home)


class TestViews(SimpleTestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse("pages:home")

    def test_books_list_GET(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
