from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('cart',views.showcart,name='cart'),
     path('orders',views.showorders,name='orders'),
     path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('remove_item/<pk>',views.remove_item_from_cart,name='remove_item_from_cart'),
    path('checkout',views.checkout_cart,name='checkout')
]