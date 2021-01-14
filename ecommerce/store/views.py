from django.shortcuts import render
from django.http import JsonResponse    
from .models import * 
from rest_framework.decorators import api_view
import json

# Create your views here.

def store(request):

    if request.user.is_authenticated:
        customer = request.user.cliente
        order, created = Pedido.objects.get_or_create(cliente=customer, completo=False)
        items = order.itempedido_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    products = Produto.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.cliente
        order, created = Pedido.objects.get_or_create(cliente=customer, completo=False)
        items = order.itempedido_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}

    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.cliente
        order, created = Pedido.objects.get_or_create(cliente=customer, completo=False)
        items = order.itempedido_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}

    context = {'items':items, 'order':order}
    return render(request, 'store/checkout.html', context)

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action: ', action)
    print('ID do produto: ', productId)
    

    customer = request.user.cliente
    product = Produto.objects.get(id=productId)
    order, created = Pedido.objects.get_or_create(cliente=customer, completo=False)
    orderItem, created = ItemPedido.objects.get_or_create(pedido=order, produto=product)

    if action == 'add':
        orderItem.quantidade = (orderItem.quantidade + 1)
    elif action == 'remove':
        orderItem.quantidade = (orderItem.quantidade - 1)

    orderItem.save()

    if orderItem.quantidade <= 0:
        orderItem.delete() 

    return JsonResponse('O item foi adicionado', safe=False)

    

