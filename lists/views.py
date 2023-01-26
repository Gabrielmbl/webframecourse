from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text','') # Replace new_item_text with whatever request.POST.get is. 
                                                        # item_text is the name of the input in home.html that gets sent to the POST
    })