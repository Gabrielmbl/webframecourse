from django.shortcuts import redirect,render
from django.http import HttpResponse

from lists.models import Item

# Create your views here.
def home_page(request):
    return render(request, 'home.html') 
 
def view_list(request):
    items = Item.objects.all() # These are the items that I have stored
    return render(request, 'list.html', {'items' : items}) 

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/') # Then it redirects and runs home_page(request) again to go now as GET
