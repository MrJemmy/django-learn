import json
from .models import *

def cookieCart(request):
    cart = request.COOKIES.get('cart')
    cart = {} if cart is None else json.loads(cart)
    print('cart :', cart)
    items = []
    order = {
        'get_cart_items': 0,
        'get_cart_total': 0,
        'shipping': False,
    }
    cartItems = 0
    for i in cart:
        quantity = cart[i]['quantity']
        cartItems += quantity
        try:
            product = Product.objects.get(id=i)
        except:
            continue
        total = product.price * quantity
        order['get_cart_total'] += total
        order['get_cart_items'] += quantity
        item = {
            'product': {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'image_url': product.image_url
            },
            'quantity': quantity,
            'get_total': total
        }
        items.append(item)
        if product.digital == False:
            order['shipping'] = True

    return {'items' : items, 'order' : order, 'cartItems' : cartItems}


def cartData(request):
    if request.user.is_authenticated:
        print(request.user)
        try:
            customer = request.user.customer  # First if user is not a customer, then
        except:
            customer, created = Customer.objects.get_or_create(user=request.user, name=request.user.username)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)  # 'get_or_create' learn more
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        items = cookieData['items']
        order = cookieData['order']
        cartItems = cookieData['cartItems']
    return {'items' : items, 'order' : order, 'cartItems' : cartItems}

def guestOrder(request, data):
    name = data['form']['name']
    email = data['form']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']

    customer, created = Customer.objects.get_or_create(
        name=name,
        email=email,
    )
    order = Order.objects.create(
        customer=customer,
        complete=False
    )
    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )
    return order, customer
