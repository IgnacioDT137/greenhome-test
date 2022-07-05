from django.urls import path
from .views import *

urlpatterns = [
    path('usuarios', getUsuarios, name='usuarios'),
    path('singleUsuario/<username>', singleUsuario, name='singleUsuario'),
    ]