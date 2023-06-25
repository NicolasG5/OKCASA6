from .models import *
from rest_framework import viewsets, permissions
from .serializers import *


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer

class TecnicoViewSet(viewsets.ModelViewSet):
    queryset = Tecnico.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TecnicoSerializer

class SolicitudEnLineaViewSet(viewsets.ModelViewSet):
    queryset = SolicitudEnLinea.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SolicitudEnLineaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
