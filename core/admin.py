from django.contrib import admin
#Importa todas las clases propias de Core
from .models import *


#Seccion donde se registran las clases al panel de admin de Django
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(EquipoInspeccion)





