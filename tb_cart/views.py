from django.shortcuts import render
from tb_shop import Product
from .models import Cart, CartItem

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id(request)
        )
        cart.save(),
    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity += 1
        cart_item..save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantitty = 1,
            cart  = cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(requestm, total=0, counter=0, cart_item= None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart,active=true)
        for cart_item in cart_items:
            total += (cart_item.product.price = cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    
    return render(request, 'cart.hmtl', dict(cart_item = cart_items, total = total, counter = counter))
