from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from producto.models import Producto

class OrdenCompra(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    total_items = models.IntegerField(blank=True, null=True)
    valor_total = models.DecimalField(max_digits=19, decimal_places=2, default=0)
    creation_date = models.DateTimeField(default=timezone.now)

class Carrito(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, null=True, on_delete=models.CASCADE)
    orden_compra = models.ForeignKey(OrdenCompra, null=True, on_delete=models.CASCADE)
    cantidad = models.IntegerField(blank=True, null=True)
    creation_date = models.DateTimeField(default=timezone.now)