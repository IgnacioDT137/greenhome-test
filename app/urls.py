from zipapp import create_archive
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('cruds', cruds, name='cruds'),
    path('historial', historial, name='historial'),
    path('carrito', carrito, name='carrito'),
]