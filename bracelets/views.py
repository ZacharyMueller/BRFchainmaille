from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item

def indexview(request):
    object_list = []
    if 'bracelet' in request.path:
        object_list = list(Item.objects.filter(item_type='br'))
    elif 'earing' in request.path:
        object_list = list(Item.objects.filter(item_type='er'))
    else:
        object_list = list(Item.objects.all())
    req_context = {
        'object_list':object_list,
    }
    return render(request, 'index.html', context=req_context)

class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'
