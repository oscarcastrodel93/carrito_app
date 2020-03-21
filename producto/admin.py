from django.contrib import admin

from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    # ...
    list_display = ('referencia', 'descripcion', 'precio')

# Register your models here.

admin.site.register(Producto, ProductoAdmin)
