from django.shortcuts import render
from django.http import JsonResponse    
from .models import * 
from rest_framework.decorators import api_view
import json

# Create your views here.

def store(request):
    products = Produto.objects.all()
    context = {'products': products}
    return render(request, 'store/store.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.cliente
        order, created = Pedido.objects.get_or_create(cliente=customer, completo=False)
        items = order.itempedido_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.cliente
        order, created = Pedido.objects.get_or_create(cliente=customer, completo=False)
        items = order.itempedido_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}

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
    return JsonResponse('O item foi adicionado', safe=False)

    customer = request.user.cliente
    product = Produto.objects.get(id=productId)
    order, created = Pedido.objects.get_or_create(cliente=customer, completo=False)

    if action == 'add':
        ItemPedido.quantidade = (ItemPedido.quantidade +1)
    elif action == 'remove':
        ItemPedido.quantidade = (ItemPedido.quantidade - 1)

    ItemPedido.save()

    if ItemPedido.quantidade <= 0:
        ItemPedido.delete() 

    orderItem, created = ItemPedido.objects.get_or_create(order=order, product=product)

