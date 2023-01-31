from django.shortcuts import redirect,render
from django.http import HttpResponse

from lists.models import Item

# Create your views here.
def home_page(request):
    # Handles POST
    if request.method == 'POST': # If method is post, it adds to my data base
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/') # Then it redirects and runs home_page(request) again to go now as GET
    else:
        new_item_text = ''

    #Handles GET
    return render(request, 'home.html') 
 
    # return render(request, 'home.html', {
    #     'new_item_text': request.POST.get('item_text','') # Replace new_item_text with whatever request.POST.get is. 
    #                                                     # item_text is the name of the input in home.html that gets sent to the POST
    # })

def view_list(request):
    items = Item.objects.all() # These are the items that I have stored
    return render(request, 'list.html', {'items' : items}) 