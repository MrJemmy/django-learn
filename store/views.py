import json

from django.shortcuts import render
from django.http import JsonResponse

from .models import *

# Create your views here.
def store(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)  # 'get_or_create' learn more
        cartItems = order.get_cart_items
    else:
        cartItems = 0
    context={'products' : products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

def cart(request):
    if request.user.is_authenticated:
        print(request.user)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)  # 'get_or_create' learn more
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_items' : 0,
            'get_cart_total' : 0,
        }
        cartItems = 0
    context={
        'items' : items,
        'order' : order,
        'cartItems' : cartItems
    }
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        print(request.user)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)  # 'get_or_create' learn more
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {
            'get_cart_items': 0,
            'get_cart_total': 0,
            'shipping' : 0
        }
        cartItems = 0
    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
    }
    return render(request, 'store/checkout.html', context)

def insert_product(request):
    context={}
    if request.method == "POST":
        query_data = request.POST
        print(query_data)
    return render(request, 'store/insert_product.html', context)

def add_item(request):
    data = json.loads(request.body) # why .body instant of .POST, .POST return Empty
    productId = data['productId']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('item was added', safe=False)

def process_order(request):
    print("data :", request.body)
    return JsonResponse('payment complete!', safe=False)