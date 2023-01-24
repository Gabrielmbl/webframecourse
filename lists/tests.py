from django.urls import resolve
# TestCase is a modification of unittest.TestCase from earlier.
from django.test import TestCase
from django.http import HttpRequest
from lists.views import home_page

class HomePageTest(TestCase):

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
