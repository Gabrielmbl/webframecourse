from django.shortcuts import redirect,render
from django.http import HttpResponse

from lists.models import Item

# Create your views here.
def home_page(request):
    # Handles POST
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    else:
        new_item_text = ''

    #Handles GET
    items = Item.objects.all()
    return render(request, 'home.html', {'items' : items})
 
    # return render(request, 'home.html', {
    #     'new_item_text': request.POST.get('item_text','') # Replace new_item_text with whatever request.POST.get is. 
    #                                                     # item_text is the name of the input in home.html that gets sent to the POST
    # })