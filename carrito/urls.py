from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.decorators import login_required
from carrito.views import *
from producto.views import ProductosSerialList

urlpatterns = [
    #BASIC VIEWS
    url(r'^$',login_required(index), name='index'),
    url(r'^carrito', login_required(verCarrito), name='verCarrito'),
    url(r'^compras', login_required(verCompras), name='verCompras'),

    #AJAX
    url(r'^ajax/agregarAlCarrito/$', login_required(agregarAlCarrito), name='agregarAlCarrito'),
    url(r'^ajax/quitarDelCarrito/$', login_required(quitarDelCarrito), name='quitarDelCarrito'),
    url(r'^ajax/vaciarCarrito/$', login_required(vaciarCarrito), name='vaciarCarrito'),
    url(r'^ajax/procesarCompra/$', login_required(procesarCompra), name='procesarCompra'),

    #API REST
    url(r'^api/productos/$', ProductosSerialList.as_view()),
    url(r'^api/carrito/$', CarritoSerialList.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)