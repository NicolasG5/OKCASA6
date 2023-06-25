from rest_framework import serializers
from .models import *


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','rut','nombres','apellidos','edad', 'direccion','telefono','tipo')
        

class TecnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnico
        fields = ('id','nombre','correo_electronico')




class SolicitudEnLineaSerializer(serializers.ModelSerializer):
    servicio_label = serializers.SerializerMethodField()

    class Meta:
        model = SolicitudEnLinea
        fields = ( 'nombre','apellido','descripcion', 'correo', 'fecha', 'hora','servicio','servicio_label', 'estado')

    def get_servicio_label(self, obj):
        servicio_label = next((choice[1] for choice in ServicioChoice.get_choices() if choice[0] == obj.servicio), '')
        return servicio_label
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

