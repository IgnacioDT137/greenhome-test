import email
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from datetime import datetime

# Create your views here.

#funcion que muestra los productos de la tienda
def home(request):
    productos = Producto.objects.all()
    return render(request, 'app/home.html', {"productos":productos})

#funcion que muestra los cruds al usuario adminisistrador
def cruds(request):
    return render(request, 'app/cruds.html')

#funcion que muestra el historial de compras
def historial(request):
    compras = Venta.objects.filter(usuario = request.session["username"])
    return render(request, 'app/historial.html', {"compras":compras})

#funcion que muestra el carrito de compras del usuario
def carrito(request):
    cart = Carrito.objects.filter(username=request.session['username'])
    cartitems = CarritoItem.objects.filter(id_carrito = Carrito.objects.get(username = request.session['username']).id_carrito)
    return render(request, 'app/carrito.html', {"cartitems":cartitems, "cart":cart})

#funcion que permite a usuario ser suscriptor de la página a cambio de una donacion mensual
def donacion(request):
    if request.method == 'POST':
        user = Usuario.objects.filter(username = request.session['username']).first()
        if not user.suscrito:
            sus = Suscripcion(
                username = request.session['username'],
                monto_mensual = request.POST['monto'],
            )
            sus.save()
            user.suscrito = True
            user.save()
        return redirect('home')
    else:
        return render(request, 'app/donaciones.html')

#funcion que mermite al usuario iniciar sesión
def loginForm(request):
    if request.method == 'POST':
        try:
            newUser = Usuario.objects.get(username = request.POST['username'], pwd = request.POST['passwordinput'])
            request.session['username'] = newUser.username 
            request.session['suscrito'] = newUser.suscrito
            return redirect('home')
        except Usuario.DoesNotExist as e:
            messages.success(request, 'Usuario o contraseña incorrectos')
            return redirect('loginForm')
    return render(request, 'app/login.html')

#funcion que permite crear un usuario nuevo
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
            Carrito(username = request.POST['username'], subtotal = 0).save()
            newUser.save()
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('loginForm')
    return render(request, 'app/registro.html')

#funcion que muestra el crud de los productos
def crudProd(request):
    productos = Producto.objects.all()
    return render(request, 'app/crudProd.html', {"productos":productos})

#funcion que muestra el crud de las promociones
def crudPromo(request):
    promos = Promocion.objects.all()
    return render(request, 'app/crudPromo.html', {"promos":promos})

#funcion que perimite crear una promocion en el crud
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

#funcion que permite borrar una promocion
def delPromo(request, code):
    promo = Promocion.objects.filter(codigo = code)
    promo.delete()
    return redirect('crudPromo')

#funcion que permite añadir un producto
def addProducto(request):
    name = request.POST['nombre']
    price = request.POST['precio']
    stock = request.POST['stock']
    img = request.POST['imagen']
    newProd = Producto(nombre = name, precio = price, stock = stock, imagen = img)
    newProd.save()
    return redirect('crudProd')        

#funcion que permite borrar un producto
def delProd(request, code):
    prod = Producto.objects.filter(id_producto = code)
    prod.delete()
    return redirect('crudProd')

#funcion que permite editar un producto existente
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

#funcion que permite editar una promocion existente
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

#funcion que permite cerrar sesión
def logout(request):
    del request.session['username']
    del request.session['suscrito']
    return redirect('loginForm')

def agregarProducto(request, user_id, prod_id):
    item = CarritoItem.objects.filter(id_carrito = Carrito.objects.get(username = user_id).id_carrito).filter(id_producto = prod_id)
    if item.exists():
        prod = Producto.objects.get(id_producto=prod_id)
        prod.stock -= 1
        prod.save()
        item = CarritoItem.objects.get(id_carrito = Carrito.objects.get(username = user_id).id_carrito, id_producto = prod_id)
        item.cantidad += 1
        item.subtotal_producto += Producto.objects.get(id_producto = prod_id).precio
        item.save()
        #actualizacion de carrito:
        subt = 0
        carrito = Carrito.objects.get(username = user_id)
        items = CarritoItem.objects.filter(id_carrito = carrito.id_carrito)
        for i in items:
            subt += i.subtotal_producto
        carrito.subtotal = subt
        carrito.save()        
    else:
        prod = Producto.objects.get(id_producto=prod_id)
        prod.stock -= 1
        prod.save()
        newItem = CarritoItem(id_carrito = Carrito.objects.get(username = user_id).id_carrito, nombre = Producto.objects.get(id_producto = prod_id).nombre , id_producto = Producto.objects.get(id_producto = prod_id).id_producto, cantidad = 1, subtotal_producto = Producto.objects.get(id_producto = prod_id).precio)
        newItem.save()
        #actualizacion de carrito:
        subt = 0
        carrito = Carrito.objects.get(username = user_id)
        items = CarritoItem.objects.filter(id_carrito = carrito.id_carrito)
        for i in items:
            subt += i.subtotal_producto
        carrito.subtotal = subt
        carrito.save()
    return redirect('home')  

def comprar(request, p_total, id_carrito):
    newVenta = Venta(usuario = request.session['username'], fecha = datetime.now(), total=p_total)
    newVenta.save()

    for item in CarritoItem.objects.filter(id_carrito = id_carrito):
        item.delete()

    cart = Carrito.objects.get(id_carrito = id_carrito)
    cart.subtotal = 0
    cart.save()

    return redirect('carrito')