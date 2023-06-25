from django.db import models
from django.utils import timezone
from datetime import time
from django.contrib.auth.models import User




# Create your models here.

class TipoUsuario(models.Model):
    tipo = models.CharField(max_length=40)
    
    def __str__(self):
        return self.tipo

class Usuario(models.Model):
    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    tipo = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombres
    
   
class Tecnico(models.Model):
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField()

    def __str__(self):
        return self.nombre

from datetime import time
from django.utils import timezone

class HistorialSolicitud(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50)


class ServicioChoice:
    CHOICES = (
        (1, 'Estudio de suelo'),
        (2, 'Montar y desmontar material'),
        (3, 'Mantenimiento y reparación'),
    )

    @classmethod
    def get_choices(cls):
        return cls.CHOICES

 

class SolicitudEnLinea(models.Model):
    
    tecnico_id = models.ForeignKey(Tecnico, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=100,default='Pendiente')
    descripcion = models.TextField()
    servicio = models.IntegerField(choices=ServicioChoice.get_choices(), default=1)


    def __str__(self):
        servicio_label = next((choice[1] for choice in ServicioChoice.get_choices() if choice[0] == self.servicio), '')
        return f"{self.descripcion} - {self.nombre} {self.apellido} ({self.correo}) - Fecha: {self.fecha} Hora: {self.hora} - Estado: {self.estado} - Servicio: {servicio_label}"

        

class controlInspeccion(models.Model):
    tecnico_id = models.ForeignKey(Tecnico, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=100, blank=True)
    apellido = models.CharField(max_length=100, blank=True)
    correo = models.EmailField(blank=True)
    fecha = models.DateField(blank=True)
    hora = models.TimeField(blank=True)
    estado = models.CharField(max_length=100,default='Pendiente')
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.descripcion} - {self.nombre} {self.apellido} ({self.correo}) - Fecha: {self.fecha} Hora: {self.hora} - Estado:{self.estado}"



class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    servicio = models.IntegerField(choices=ServicioChoice.get_choices(), default=1)
    fecha = models.DateTimeField(auto_now_add=True)
    nombre_servicio = models.CharField(max_length=100, blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        servicio_label = next((choice[1] for choice in ServicioChoice.get_choices() if choice[0] == self.servicio), '')
        return f"{self.usuario.username} - {self.servicio}"

