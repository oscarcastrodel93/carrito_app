from django.contrib import admin

from .models import OrdenCompra

class OrdenCompraAdmin(admin.ModelAdmin):
    # ...
    list_display = ('id', 'total_items', 'valor_total', 'user', 'creation_date')

# Register your models here.

admin.site.register(OrdenCompra, OrdenCompraAdmin)
