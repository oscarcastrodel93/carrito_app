from rest_framework import serializers
from django.contrib.auth.models import User
from carrito.models import Carrito

class CarritoSerializers(serializers.ModelSerializer):

    class Meta:
        model = Carrito
        fields = (
            'id', 
            'image', 
            'descripcion', 
            'user'
            ) 