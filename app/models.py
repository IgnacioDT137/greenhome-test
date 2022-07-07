from django.db import models
from datetime import datetime
# Create your models here.

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    precio = models.IntegerField(null=False)
    stock = models.IntegerField(null=False)
    imagen = models.CharField(max_length=1000, default='imagen')

class Usuario(models.Model):
    username = models.CharField(primary_key=True, max_length=30)
    email = models.EmailField(null=False, unique=True)
    pwd = models.CharField(max_length=12, null=False)
    suscrito = models.BooleanField(null=False, default=False)

class Promocion(models.Model):
    id_promocion = models.AutoField(primary_key=True)
    codigo = models.CharField(max_length=8, null=False, unique=True)
    pct = models.FloatField(null=False)
    fecha_inicio = models.DateField(null=False)
    fecha_fin = models.DateField(null=False)

class Suscripcion(models.Model):
    id_suscripcion = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    monto_mensual = models.IntegerField(null=False)
    fecha = models.DateTimeField(null=False, default=datetime.now())

class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, null=False)
    subtotal = models.IntegerField(null=False)

class CarritoItem(models.Model):
    id_carrito = models.IntegerField(null=False)
    id_producto = models.IntegerField(null=False)
    nombre = models.CharField(null=False, max_length=30)
    cantidad = models.IntegerField(null = False)
    subtotal_producto = models.IntegerField(null=False)

class Venta(models.Model):
    id_venta = models.AutoField(primary_key=True)
    usuario = models.CharField(null=False, max_length=100)
    fecha = models.DateField(null=False)
    total = models.FloatField(null=False)