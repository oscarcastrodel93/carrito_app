from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Producto(models.Model):
    referencia = models.CharField(null=True,max_length=255)
    descripcion = models.CharField(null=True,max_length=255)
    precio = models.DecimalField(max_digits=19, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now())