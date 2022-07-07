from django.urls import path
from .views import *

urlpatterns = [
    path('usuarios', getUsuarios, name='usuarios'),
    path('suscripciones', getSus, name='suscripciones'),
    path('singleUsuario/<username>', singleUsuario, name='singleUsuario'),
    ]