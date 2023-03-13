from django.core.exceptions import ValidationError
from django.urls import resolve
# TestCase is a modification of unittest.TestCase from earlier.
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page
from lists.models import Item, List



class ListAndItemModelsTest(TestCase):
    
    def test_saving_and_retrieving_items(self):

        list_ = List()
        list_.save()

        #saving step
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)
        
        #retrieving step
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)

    def test_cannot_equal_empty_list(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save() #SQLite fails to tell us TextField is blank.
            item.full_clean() # Make sure if item is valid or not
