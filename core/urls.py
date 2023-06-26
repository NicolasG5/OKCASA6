from django.urls import path,include
from .views import *
from rest_framework import routers, serializers, viewsets
from django.contrib.auth import views as auth_views
from . import views
from .api import *
from rest_framework import routers, serializers, viewsets
from .views import RegisterView

router = routers.DefaultRouter()
#Api
router.register('api/Usuario', UsuarioViewSet, 'Usuario'),
router.register('api/Tecnico', TecnicoViewSet, 'Tecnico')
router.register(r'api/SolicitudEnLinea', SolicitudEnLineaViewSet, basename='SolicitudEnLinea')
router.register(r'api/User', UserViewSet, basename='User')

urlpatterns = [
    path('', index, name="index"),
    path('indexapi/', indexapi, name="indexapi"),
    path('base/', base, name="base"),
    path('blog/', blog, name="blog"),
    path('correo/', correo, name="correo"),
    path('detalles/', detalles, name="detalles"),
    path('equipo/', equipo, name="equipo"),
    path('enviar_correo/', enviar_correo, name="enviar_correo"),
    path('servicio/', servicio, name="servicio"),
    path('sobrenosotros/', sobrenosotros, name="sobrenosotros"),
    path('testimonios/', testimonios, name="testimonios"),
    path('perfil/', perfil, name="perfil"),
    path('testimonios/', testimonios, name="testimonios"),
    path('seguimientoSolicitud/', seguimientoSolicitud, name="seguimientoSolicitud"),
    path('solicitud/', solicitud, name="solicitud"),
    path('historial/', historial, name="historial"),
    path('formulariocorreo/', formulariocorreo, name="formulariocorreo"),
    path('tecnico/', tecnico, name="tecnico"),
    path('solicitudtecnico/', solicitudtecnico, name="solicitudtecnico"),
    path('inspeccion/', inspeccion, name="inspeccion"),
    path('apiauth/', include('rest_framework.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('solicitud/<int:solicitud_id>/confirmar/', ConfirmarSolicitudView.as_view(), name='confirmar_solicitud'),
    path('solicitud/<int:solicitud_id>/denegar/', DenegarSolicitudView.as_view(), name='denegar_solicitud'),
    path('solicitud/<int:solicitud_id>/modificar/', views.modificar_solicitud, name='modificar_solicitud'),
    path('solicitud/<int:solicitud_id>/eliminar/', views.eliminar_solicitud, name='eliminar_solicitud'),
    path('equiposDisponible/', equiposDisponible, name='equiposDisponible'),
    

]
urlpatterns += router.urls