import datetime
import json

from django.shortcuts import render
from django.http import JsonResponse

from .models import *
from .utils import cookieCart, cartData, guestOrder
# Create your views here.
def store(request):
    products = Product.objects.all()
    data = cartData(request)
    context={'products' : products, 'cartItems':data['cartItems']}
    return render(request, 'store/store.html', context)

def cart(request):
    data = cartData(request)
    context = {
        'items': data['items'],
        'order': data['order'],
        'cartItems': data['cartItems'],
    }
    return render(request, 'store/cart.html', context)

def checkout(request):
    data = cartData(request)
    context = {
        'items': data['items'],
        'order': data['order'],
        'cartItems': data['cartItems'],
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
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        print('process_order for not logged in user')
        print('COOKIES:', request.COOKIES)
        order, customer = guestOrder(request,data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == float(order.get_cart_total):
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('payment complete!', safe=False)