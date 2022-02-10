from django.urls import path
from .views import Home
from bracelets.views import indexview, ItemDetailView

urlpatterns = [
    path('', Home, name='home'),
    path('stock/', indexview, name='all_stock'),
    path('stock/bracelets', indexview, name='bracelet_stock'),
    path('stock/earings', indexview, name='earing_stock'),
    path('stock/item/<int:pk>/', ItemDetailView.as_view(), name='detail')
] 