from rest_framework.serializers import ModelSerializer
from app.models import Usuario

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'pwd', 'suscrito']