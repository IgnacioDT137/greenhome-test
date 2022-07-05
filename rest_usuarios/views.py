from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from app.models import Usuario
from .serializer import UsuarioSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here.

@csrf_exempt
@api_view(['GET'])
def getUsuarios(request):
    usuarios = Usuario.objects.all()
    serializer = UsuarioSerializer(usuarios, many=True)
    return Response(serializer.data)

@csrf_exempt
@api_view(['GET', 'POST', 'DELETE'])
def singleUsuario(request, username):
    if request.method == 'GET':
        usuario = Usuario.objects.get(username = username)
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        usuario = Usuario.objects.filter(username = username).first()
        usuario.delete()
        return Response('Usuario eliminado')
    

    