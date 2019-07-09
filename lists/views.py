from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request,
                  'lists/home.html',
                  {'new_item_text': request.POST.get('item_text', '')})

# POST.get('key', val) - если запрос не POST['key']=val, то тогда вернуть GET



