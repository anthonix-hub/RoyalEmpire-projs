from concurrent.futures import process
from itertools import product
import json
from multiprocessing import context
from rlcompleter import Completer
from django.http import JsonResponse
from django.shortcuts import render

from Royalemp_commerce.models import Order, OrderItem, Product



def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        
        order, created = Order.objects.get_or_create(customer=customer, complete=False )
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cart = json.loads(request.COOKIES['cart'])
        print('cart:', cart)
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']
        
        for i in cart:
            cartItems += cart[i]["quantity"]
            
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])
            
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']
            
            item = {
                'product':{
                    'id':product.id,
                    'name':product.name,
                    'price':product.price,
                    'imageURL':product.imageURL,
                },
                'quantity':cart[i]['quantity'],
                'get_total':total,
            }
            items.append(item)
    
    product_items = Product.objects.all()
    
    context={
        'product_items':product_items,
        'cartItems':cartItems, 
    }
    return render(request, 'Royalemp_commerce/store.html',context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False )
        items = order.orderitem_set.all
        cartItems = order.get_cart_items
    else:
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:        
            cart = {}
        print('cart:', cart)
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']
        
        for i in cart:
            cartItems += cart[i]["quantity"]
            
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])
            
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']
            
            item = {
                'product':{
                    'id':product.id,
                    'name':product.name,
                    'price':product.price,
                    'imageURL':product.imageURL,
                },
                'quantity':cart[i]['quantity'],
                'get_total':total,
            }
            items.append(item)
         
    context={
        'items':items,
        'order':order,
        'cartItems':cartItems,
    }
    return render(request, 'Royalemp_commerce/cart.html',context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False )
        items = order.orderitem_set.all
        cartItems = order.get_cart_items
    else:
        # cart = json.loads(request.COOKIES['cart'])
        # print('cart:', cart)
        try:
            cart = json.loads(request.COOKIES['cart'])
        except:        
            cart = {}
        print('cart:', cart)
        items = []
        order = {'get_cart_total':0,'get_cart_item':0, 'shipping':False, }
        cartItems = order['get_cart_items']
        # cartItems = order[]
        
        for i in cart:
            cartItems += cart[i]["quantity"]
            
            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])
            
            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']
            
            item = {
                'product':{
                    'id':product.id,
                    'name':product.name,
                    'price':product.price,
                    'imageURL':product.imageURL,
                },
                'quantity':cart[i]['quantity'],
                'get_total':total,
            }
            items.append(item)
        
    context={
        'items':items,
        'order':order,
        "cartItems":cartItems,
    }
    return render(request, 'Royalemp_commerce/checkout.html',context)

def views(request):
    
    context = {
        
    }
    return render(request, 'Royalemp_commerce/views.html', context)

def updateItem(request):
    data = json.loads(request.body)    
    productId = data['productId']
    action = data['action']
    
    print('Action:', action)
    print('ProductId:', productId)
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete = False)
    
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    
    elif action == 'clear':
        orderItem.quantity = 0
        
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
    
    return JsonResponse('item was added', safe=False)


def store_cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        
        order, created = Order.objects.get_or_create(customer=customer, complete=False )
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}
        cartItems = order['get_cart_items']
        
    
    product_items = Product.objects.all()
    
    context={
        'product_items':product_items,
        'cartItems':cartItems, 
    }
    return render(request, 'Royalemp_commerce/main.html',context)

