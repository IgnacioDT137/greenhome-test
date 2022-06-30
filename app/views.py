from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    productos = Producto.objects.all()
    return render(request, 'app/home.html', {"productos":productos})

def cruds(request):
    return render(request, 'app/cruds.html')

def historial(request):
    return render(request, 'app/historial.html')

def carrito(request):
    return render(request, 'app/carrito.html')

def donacion(request):
    return render(request, 'app/donaciones.html')

def loginForm(request):
    return render(request, 'app/login.html')

def regForm(request):
    return render(request, 'app/registro.html')