from rest_framework import serializers
from django.contrib.auth.models import User
from producto.models import Producto

class ProductoSerializers(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = (
            'id', 
            'referencia', 
            'descripcion', 
            'precio', 
            'creation_date'
        ) 