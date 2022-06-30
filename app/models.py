from django.db import models

# Create your models here.

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=False)
    precio = models.IntegerField(null=False)
    stock = models.IntegerField(null=False)

class Usuario(models.Model):
    username = models.CharField(primary_key=True, max_length=30)
    email = models.EmailField(null=False)
    pwd = models.CharField(max_length=12, null=False)

class Promocion(models.Model):
    id_promocion = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=8, null=False)
    pct = models.FloatField(null=False)
    fecha_inicio = models.DateField(null=False)
    fecha_fin = models.DateField(null=False)
