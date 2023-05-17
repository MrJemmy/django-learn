from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
    products = Product.objects.all()
    context={'products' : products}
    return render(request, 'store/store.html', context)

def cart(request):
    context={}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context={}
    return render(request, 'store/checkout.html', context)

def insert_product(request):
    context={}
    if request.method == "POST":
        query_data = request.POST
        print(query_data)
    return render(request, 'store/insert_product.html', context)
