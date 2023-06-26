from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.conf import settings
from OKcasa2.settings import EMAIL_HOST_PASSWORD, EMAIL_HOST_USER
from rest_framework import viewsets
from .models import *
from .forms import SolicitudEnLineaForm, RegisterForm, RegisterView
import json
import requests
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Tecnico, Compra
from .api import UsuarioViewSet, TecnicoViewSet, SolicitudEnLineaViewSet
from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework import routers, serializers, viewsets
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.http import HttpResponse
import socket
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.http import HttpResponse





# Create your views here.

def grupo_requerido(nombre_grupo):
    def decorator(view_func):
        @user_passes_test(lambda user: user.groups.filter(name=nombre_grupo).exists())
        def wrapper(request, *args , **kwargs):
            return view_func(request, *args , **kwargs)
        return wrapper
    return decorator

@grupo_requerido('Cliente')
def index(request):
    return render(request,'core/index.html')



@grupo_requerido('Cliente')
@login_required
def indexapi(request):

    respuesta = requests.get('https://mindicador.cl/api/')

    monedas = respuesta.json()

    data = {
        'monedas': monedas,
    }

    return render(request,'core/indexapi.html',data)

@login_required
def base(request):
    user_is_tecnico = False
    if request.user.is_authenticated and request.user.groups.filter(name='tecnico').exists():
        user_is_tecnico = True
    return render(request,'core/base.html',{'user_is_tecnico': user_is_tecnico})

@login_required
def formulariocorreo(request):
    return render(request,'core/formulariocorreo.html')

@grupo_requerido('Cliente')
@login_required
def blog(request):
    return render(request,'core/blog.html')

@grupo_requerido('Cliente')
@login_required
def contacto(request):
    return render(request,'core/contacto.html')

@grupo_requerido('Cliente')
@login_required
def detalles(request):
    return render(request,'core/detalles.html')


@login_required
def inspeccion(request):
    return render(request,'core/inspeccion.html')

@login_required
def equipo(request):
    return render(request,'core/equipo.html')

@grupo_requerido('Cliente')
@login_required
def servicio(request):
    return render(request,'core/servicio.html')

@grupo_requerido('Cliente')
@login_required
def sobrenosotros(request):
    return render(request,'core/sobrenosotros.html')

@grupo_requerido('Cliente')
@login_required
def testimonios(request):
    return render(request,'core/testimonios.html')


@login_required
def correo(request):
    return render(request,'core/correo.html')

@grupo_requerido('Cliente')
@login_required
def perfil(request):
    return render(request,'core/perfil.html')


@login_required
def seguimientoSolicitud(request):
    return render(request,'core/seguimientoSolicitud.html')

@grupo_requerido('Cliente')
@login_required
def equiposDisponible(request):
    equipos = EquipoInspeccion.objects.all()
    return render(request,'core/equiposDisponible.html',{'equipos': equipos})


@login_required
def solicitud(request):
    if request.method == 'POST':
        form = SolicitudEnLineaForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            tecnico = Tecnico.objects.first()
            solicitud.tecnico = tecnico
            solicitud.save()
            return redirect('solicitud')  # Corregido el argumento de redirect
    else:
        form = SolicitudEnLineaForm()
    
    return render(request, 'core/solicitud.html', {'form': form})


@login_required
@grupo_requerido('tecnico')
def tecnico(request):

    

    
    tecnico = Tecnico.objects.first()  # Corregir la asignación de la variable "tecnico" en minúsculas
    solicitudes = SolicitudEnLinea.objects.filter(tecnico_id=tecnico)
    return render(request, 'core/tecnico.html', {'tecnico': tecnico, 'solicitudes': solicitudes})


@login_required
@grupo_requerido('tecnico')
def solicitudtecnico(request):
    return render(request,'core/solicitudtecnico.html')


class Usuarioapiview(View):
    def get (self,request):
        Listar = Usuario.objects.values()
        return JsonResponse(list(Listar),safe=False)

class ConfirmarSolicitudView(View):
    def post(self, request, solicitud_id):
        # Lógica para confirmar la solicitud con el ID especificado
        solicitud = SolicitudEnLinea.objects.get(id=solicitud_id)
        solicitud.estado = 'confirmado'
        solicitud.save()
        return JsonResponse({'status': 'success'})

class DenegarSolicitudView(View):
    def post(self, request, solicitud_id):
        # Lógica para denegar la solicitud con el ID especificado
        solicitud = SolicitudEnLinea.objects.get(id=solicitud_id)
        solicitud.estado = 'denegado'
        solicitud.save()
        
        return JsonResponse({'status': 'success'})


def modificar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudEnLinea, id=solicitud_id)
    if request.method == 'POST':
        form = SolicitudEnLineaForm(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            return redirect('tecnico')  # Reemplaza 'nombre-de-la-vista' con el nombre de tu vista de tabla de solicitudes
    else:
        form = SolicitudEnLineaForm(instance=solicitud)
    return render(request, 'core/solicitud.html', {'form': form})

def eliminar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(SolicitudEnLinea, id=solicitud_id)
    if request.method == 'POST':
        solicitud.delete()
        return redirect('tecnico')  # Reemplaza 'nombre-de-la-vista' con el nombre de tu vista de tabla de solicitudes
    return render(request, 'core/tecnico.html', {'solicitud': solicitud})


def payment_success(request):
    servicio = 'nombre_del_servicio'  # Reemplaza 'nombre_del_servicio' con el nombre o descripción del servicio que se compró
    Compra.objects.create(servicio=servicio)
    return redirect('historial_compras')


def historial(request):
    compras = Compra.objects.filter(usuario=request.user).order_by("-fecha")
    return render(request, 'core/historial.html', {'compras': compras})
    # Redireccionar o mostrar un mensaje de éxito al usuario

def get_all_users(request):
    users = User.objects.all().values()
    return JsonResponse({"users": list(users)})


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

# Resto de las importaciones...
@login_required
def enviar_correo(request):
    if request.method == 'POST':
        solicitud_id = request.POST.get('solicitud_id')
        # Obtener los datos de la solicitud
        solicitud = SolicitudEnLinea.objects.get(id=solicitud_id)

        if solicitud.estado == 'confirmado':
            subject = 'Asunto del correo'  # Reemplaza esto con el asunto deseado
            message = f'Hola {solicitud.nombre}, tu solicitud ha sido confirmada.'  # Reemplaza esto con el mensaje deseado
            from_email = settings.EMAIL_HOST_USER  # Reemplaza esto con tu dirección de correo electrónico
            recipient_list = [solicitud.correo]

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        elif solicitud.estado == 'denegado':
            subject = 'Asunto del correo'  # Reemplaza esto con el asunto deseado
            message = f'Hola {solicitud.nombre}, tu solicitud ha sido denegada.'  # Reemplaza esto con el mensaje deseado
            from_email = settings.EMAIL_HOST_USER  # Reemplaza esto con tu dirección de correo electrónico
            recipient_list = [solicitud.correo]

            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
        request.session['correo_enviado'] = True
        # Redirigir a la página de solicitud después de enviar el correo
        return redirect('tecnico')  # Reemplaza 'ruta_de_la_vista_de_solicitudes' con la ruta real de tu vista de solicitudes

    # Manejar otros casos, como el método de solicitud incorrecto
    return render(request, 'core/tecnico.html', {'correo_enviado': request.session.get('correo_enviado', False)})  # Redirigir a la página de solicitud si ocurre algún error

        

      
   



    # Resto de la lógica de la vista...


    # Realiza las acciones necesarias para manejar el error, como mostrar un mensaje de error al usuario o registrar el error en un archivo de registro.


        # Redirigir a la página de éxito o mostrar un mensaje de confirmación en la misma página

    # Resto de la lógica de la vista...

        
# #Historial de solicictudes
# def historial_solicitud(request):
#     #crea el historial
#     historial = HistorialSolicitud(estado='Enviada')
#     historial.save()

#     #Asocia el historial

#     solitud= SolicitudEnLinea


    # return 'core/index.html'