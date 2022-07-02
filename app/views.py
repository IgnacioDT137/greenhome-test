import email
from django.shortcuts import redirect, render
from django.contrib import messages
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
    if request.method == 'POST':
        try:
            newUser = Usuario.objects.get(username = request.POST['username'], pwd = request.POST['passwordinput'])
            request.session['username'] = newUser.username 
            return redirect('home')
        except Usuario.DoesNotExist as e:
            messages.success(request, 'Usuario o contraseña incorrectos')
            return redirect('loginForm')
    return render(request, 'app/login.html')

def regForm(request):
    if request.method == 'POST':
        if Usuario.objects.filter(email = request.POST['email']).exists(): 
            messages.success(request, 'El email ingresado ya esta registrado')
        elif Usuario.objects.filter(username = request.POST['username']).exists(): 
            messages.success(request, 'El usuario ingresado ya esta registrado')
        else:
            newUser = Usuario(
                username = request.POST['username'],
                email = request.POST['email'],
                pwd = request.POST['pwd']
            )
            newUser.save()
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('loginForm')
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

def editProd(request, code):
    producto = Producto.objects.filter(id_producto = code)
    if request.method == 'POST':
        oldProd = Producto.objects.get(id_producto = code)
        if request.POST['newname'] != '':
            oldProd.nombre = request.POST['newname']
            oldProd.save()
        if str(request.POST['newprice']) != '':
            oldProd.precio = request.POST['newprice']
            oldProd.save()
        if str(request.POST['newstock']) != '':
            oldProd.stock = request.POST['newstock']
            oldProd.save()
        if request.POST['newimage'] != '':
            oldProd.imagen = request.POST['newImage']
            oldProd.save()
        return redirect('crudProd')
    else:        
        return render(request, 'app/editProd.html', {"producto":producto})

def editPromo(request, code):
    promo = Promocion.objects.filter(id_promocion = code)
    if request.method == 'POST':
        oldPromo = Promocion.objects.get(id_promocion = code)
        if request.POST['newcode'] != '':
            oldPromo.codigo = request.POST['newcode']
            oldPromo.save()
        if str(request.POST['newpct']) != '':
            oldPromo.pct = request.POST['newpct']
            oldPromo.save()
        if str(request.POST['newstart']) != '':
            oldPromo.fecha_inicio = request.POST['newstart']
            oldPromo.save()
        if request.POST['newend'] != '':
            oldPromo.fecha_fin = request.POST['newend']
            oldPromo.save()
        return redirect('crudPromo')
    else:        
        return render(request, 'app/editPromo.html', {"promo":promo})        

def logout(request):
    del request.session['username']
    return redirect('loginForm')