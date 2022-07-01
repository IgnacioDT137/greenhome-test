from zipapp import create_archive
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('cruds', cruds, name='cruds'),
    path('historial', historial, name='historial'),
    path('carrito', carrito, name='carrito'),
    path('donar', donacion, name='donar'),
    path('loginForm', loginForm, name='loginForm'),
    path('regForm', regForm, name='regForm'),
    path('crudProd', crudProd, name='crudProd'),
    path('crudPromo', crudPromo, name='crudPromo'),
    path('addPromo', addPromo, name='addPromo'),
    path('delPromo/<code>', delPromo, name='delPromo'),
    path('addProducto', addProducto, name='addProducto'),
    path('delPro/<code>', delProd, name='delProd'),
]