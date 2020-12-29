from django.shortcuts import render
from .models import * 

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
    context = {}
    return render(request, 'store/checkout.html', context)