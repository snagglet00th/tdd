from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_test_uses_home_templates(self):
        response = self.client.get('/')  # клиент Django
        # это медод Django TestCase, который сравнивает результат запроса с правым аргументом
        self.assertTemplateUsed(response, 'lists/home.html')
