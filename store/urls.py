from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('insert_product/', views.insert_product, name='insert_product'),

    path('add_item/', views.add_item, name='add_item'),
    path('cart/add_item/', views.add_item, name='add_item'),
    path('process_order/', views.process_order, name='process_order'),
]