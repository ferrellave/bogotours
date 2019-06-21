from django.contrib import admin

from .models import *

class ProductosAdmin(admin.ModelAdmin):

    list_display = ('titulo', 'categoria', 'marca', 'creado')

admin.site.register(Producto, ProductosAdmin)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Blog)