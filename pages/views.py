from django.views.generic import TemplateView
from django.shortcuts import render
from bracelets.models import Item
from config.settings import SECRET_KEY, DEBUG

def Home(request):
    items = list(Item.objects.all()[:2])
    context = {
        'featured_items': items,
        'test': DEBUG,
    }
    return render(request, 'home.html', context=context)