from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('complete', views.complete, name='complete'),
    path('update_item', views.updateItem, name='update_item'),
    path('<season>', views.home, name='home'),
    path('item/<id>', views.item, name='item'),
    path('items/<season>/<gender>/<type>/<brand>', views.items, name='items'),
    
]
