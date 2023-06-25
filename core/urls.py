from django.urls import path
from .views import index,base,blog,contacto,detalles,equipo,servicio,sobrenosotros,testimonios,logeado

urlpatterns = [
    path('', index, name="index"),
    path('base/', base, name="base"),
    path('blog/', blog, name="blog"),
    path('contacto/', contacto, name="contacto"),
    path('detalles/', detalles, name="detalles"),
    path('equipo/', equipo, name="equipo"),
    path('servicio/', servicio, name="servicio"),
    path('sobrenosotros/', sobrenosotros, name="sobrenosotros"),
    path('testimonios/', testimonios, name="testimonios"),
    path('logeado/', logeado, name="logeado")
]
