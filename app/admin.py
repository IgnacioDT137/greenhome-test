from atexit import register
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Producto)
admin.site.register(Promocion)
admin.site.register(Usuario)
admin.site.register(Carrito)
admin.site.register(Venta)