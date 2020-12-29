from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200, null=True)
    preco = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    objects = models.Manager()
    #image

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    data_pedido = models.DateTimeField(auto_now_add=True)
    completo = models.BooleanField(default=False, null=True, blank=False)
    id_transacao = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
     
class ItemPedido(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, blank=True, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, blank=True, null=True)
    quantidade = models.IntegerField(default=0, null=True, blank=True)
    data_pedido = models.DateTimeField(auto_now_add=True)

class LocalEntrega(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, blank=True, null=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, blank=True, null=True)
    endereco = models.CharField(max_length=200, null=True)
    cidade = models.CharField(max_length=200, null=True)
    estado = models.CharField(max_length=200, null=True)
    cep = models.CharField(max_length=200, null=True)
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.endereco