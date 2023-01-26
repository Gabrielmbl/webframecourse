from django.urls import resolve
# TestCase is a modification of unittest.TestCase from earlier.
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page
from lists.models import Item

class HomePageTest(TestCase):

    def test_saving_and_retrieving_items(self):
        #saving step
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        #retrieving step
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')


    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_uses_home_template(self):
        # request = HttpRequest() 
        # response = home_page(request)
        response = self.client.get('/') # When testing, ask Django to look at this page> Whatever comes from the slash and confirm that the thing that generates is really just home.html

        # html = response.content.decode('utf8')
        # self.assertTrue(html.startswith('<html>'))
        # self.assertIn('<title>To-Do lists</title>', html)
        # self.assertTrue(html.strip().endswith('</html>')) #Strip gets rid of white spaces on the left and right

        self.assertTemplateUsed(response, 'home.html')
    
    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')

# Create your tests here.
