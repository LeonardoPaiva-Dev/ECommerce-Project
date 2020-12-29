from django.contrib import admin
from .models import *

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Pedido)
admin.site.register(ItemPedido)
admin.site.register(LocalEntrega)
