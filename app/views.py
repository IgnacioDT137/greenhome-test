from django.shortcuts import redirect, render
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

def crudProd(request):
    productos = Producto.objects.all()
    return render(request, 'app/crudProd.html', {"productos":productos})

def crudPromo(request):
    promos = Promocion.objects.all()
    return render(request, 'app/crudPromo.html', {"promos":promos})

def addPromo(request):
    try:
        code = request.POST['codigo']
        porc = request.POST['porcentaje']
        inicio = request.POST['fecha_inicio']
        fin = request.POST['fecha_fin']
        newPromo = Promocion(codigo = code, pct = porc, fecha_inicio = inicio, fecha_fin = fin)
        newPromo.save()
        return redirect('crudPromo')
    except:
        print('ocurrio un error')
        return redirect('crudPromo')

def delPromo(request, code):
    promo = Promocion.objects.filter(codigo = code)
    promo.delete()
    return redirect('crudPromo')

def addProducto(request):
    name = request.POST['nombre']
    price = request.POST['precio']
    stock = request.POST['stock']
    img = request.POST['imagen']
    newProd = Producto(nombre = name, precio = price, stock = stock, imagen = img)
    newProd.save()
    return redirect('crudProd')

        

def delProd(request, code):
    prod = Producto.objects.filter(id_producto = code)
    prod.delete()
    return redirect('crudProd')