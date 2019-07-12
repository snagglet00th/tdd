from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from lists.models import Item
from lists.views import home_page


class HomePageTest(TestCase):

    def setUp(self):
        self.FIRST_LIST_ITEM = 'A new list item'

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_uses_home_templates(self):
        response = self.client.get('/')  # клиент Django
        # это медод Django TestCase, который сравнивает результат запроса с правым аргументом
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_can_save_a_post_request(self):
        response = self.client.post('/', data={'item_text': self.FIRST_LIST_ITEM})

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()  # or Item.objects.all()[0]
        self.assertEqual(new_item.text, self.FIRST_LIST_ITEM)

        self.assertIn(self.FIRST_LIST_ITEM, response.content.decode())
        self.assertTemplateUsed(response, 'lists/home.html')


class ItemModelTest(TestCase):

    FIRST_ITEM_VALUE = "first list item"
    SECOND_ITEM_VALUE = "second list item"

    def test_saving_and_retrieving_items(self):

        first_item = Item()
        first_item.text = self.FIRST_ITEM_VALUE
        first_item.save()

        second_item = Item()
        second_item.text = self.SECOND_ITEM_VALUE
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        first_saved_item = saved_items[0]
        second_saved_items = saved_items[1]
        self.assertEqual(first_saved_item.text, self.FIRST_ITEM_VALUE)
        self.assertEqual(second_saved_items.text, self.SECOND_ITEM_VALUE)
