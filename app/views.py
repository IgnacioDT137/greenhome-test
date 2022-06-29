from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

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