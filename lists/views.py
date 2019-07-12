from django.http import HttpResponse
from django.shortcuts import render, redirect

from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        new_item = request.POST['item_text']
        Item.objects.create(text=new_item)
        return redirect('/')

    return render(request, 'lists/home.html')

# POST.get('key', val) - если запрос не POST['key']=val, то тогда вернуть GET
