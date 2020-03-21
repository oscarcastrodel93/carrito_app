from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from carrito.models import *
from carrito.serializers import CarritoSerializers
from rest_framework import generics
import json
from django.core.serializers.json import DjangoJSONEncoder

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('nombre')
        last_name = request.POST.get('apellido')
        email = request.POST.get('email')
        confirm_password = request.POST.get('confirm-password')
        if request.POST.get('login-submit'):
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
            return HttpResponseRedirect(reverse('index'))
        elif request.POST.get('register-submit'):
            if password != confirm_password:
                    return HttpResponse("Credenciales incorrectas")
            usuario_creado = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'base/login.html')
        
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('userLogin'))

def index(request):
    return render(request, 'base/index.html', {})

def agregarAlCarrito(request):
    try:
        producto = json.loads(request.POST.get('producto', {}))
        from carrito.models import Carrito
        from producto.models import Producto

        item_carrito = Carrito()
        item_carrito.user = request.user
        item_carrito.producto_id = producto.get('id')
        item_carrito.cantidad = producto.get('cantidad', 1)
        item_carrito.save()

        response = {"ok": True, "msg": "Producto agregado al carrito!"}
    except Exception as e:
        response = {"ok": False, "msg": "No se pudo agregar el producto"}
    return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder), content_type='application/json')

def quitarDelCarrito(request):
    try:
        id_carrito = json.loads(request.POST.get('id_carrito', {}))
        from carrito.models import Carrito

        item_carrito = Carrito.objects.filter(id=id_carrito).delete()

        response = {"ok": True, "msg": "Item eliminado al carrito!"}
    except Exception as e:
        response = {"ok": False, "msg": "No se pudo eliminar el item"}
    return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder), content_type='application/json')

def vaciarCarrito(request):
    try:
        from carrito.models import Carrito
        item_carrito = Carrito.objects.filter(user=request.user).delete()
        response = {"ok": True, "msg": "Items eliminados!"}
    except Exception as e:
        response = {"ok": False, "msg": "No se pudo vaciar el carrito"}
    return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder), content_type='application/json')
    

def verCarrito(request):
    from carrito.models import Carrito
    items_carrito = Carrito.objects.filter(user=request.user.id, orden_compra__isnull=True)
    result = []
    for item in items_carrito:
        result.append({
            'id': item.id,
            'referencia': item.producto.referencia,
            'descripcion': item.producto.descripcion,
            'precio': item.producto.precio,
            'cantidad': item.cantidad,
        })
    data = {
        'items_carrito': json.dumps(result, cls=DjangoJSONEncoder)
    }
    return render(request, 'carrito.html', data)

def procesarCompra(request):
    try:
        items_carrito = json.loads(request.POST.get('items_carrito', "[]"))
        from carrito.models import Carrito, OrdenCompra

        # Actualizar cantidades, sumar total
        total = 0
        for item in items_carrito:
            total += float(item.get("precio")) * item.get("cantidad")
            Carrito.objects.filter(id=item.get('id')).update(cantidad=item.get("cantidad"))

        # Crear orden de compra
        oc = OrdenCompra()
        oc.total_items = len(items_carrito)
        oc.valor_total = total
        oc.user = request.user
        oc.save()

        # Setear orden de compra para los items del carrito
        Carrito.objects.filter(user=request.user, orden_compra__isnull=True).update(orden_compra=oc)

        response = {"ok": True, "msg": "Compra realizada!"}
    except Exception as e:
        print(e)
        response = {"ok": False, "msg": "No se pudo realizar la compra."}
    return HttpResponse(json.dumps(response, cls=DjangoJSONEncoder), content_type='application/json')

def verCompras(request):
    from carrito.models import OrdenCompra, Carrito
    compras = OrdenCompra.objects.filter(user=request.user.id)
    result = []
    for compra in compras:
        items = Carrito.objects.filter(orden_compra=compra)
        items_compra = []
        for item in items:
            items_compra.append({
                'id': item.id,
                'referencia': item.producto.referencia,
                'descripcion': item.producto.descripcion,
                'precio': item.producto.precio,
                'cantidad': item.cantidad,
            })
        result.append({
            'id': compra.id,
            'total_items': compra.total_items,
            'valor_total': compra.valor_total,
            'creation_date': compra.creation_date,
            'items_compra': items_compra,
        })
    data = {
        'compras': json.dumps(result, cls=DjangoJSONEncoder)
    }
    return render(request, 'compras.html', data)

class CarritoSerialList(generics.ListCreateAPIView):
    serializer_class = CarritoSerializers
    def get_queryset(self):
        user = self.request.user
        return Carrito.objects.filter(user=user, orden_compra__isnull=True)