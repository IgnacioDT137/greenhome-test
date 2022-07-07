from rest_framework.serializers import ModelSerializer
from app.models import Usuario, Suscripcion

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'pwd', 'suscrito']

class SuscripcionSerializer(ModelSerializer):
    class Meta:
        model = Suscripcion
        fields = ['username', 'monto_mensual', 'fecha']