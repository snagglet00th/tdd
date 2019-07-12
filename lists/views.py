from django.http import HttpResponse
from django.shortcuts import render

from lists.models import Item


def home_page(request):
    item = Item()
    item.text = request.POST.get('item_text', '')
    item.save()
    return render(request,
                  'lists/home.html', {'new_item_text': item.text
                                      })

# POST.get('key', val) - если запрос не POST['key']=val, то тогда вернуть GET
