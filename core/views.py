from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def base(request):
    return render(request,'core/base.html')

def blog(request):
    return render(request,'core/blog.html')

def contacto(request):
    return render(request,'core/contacto.html')

def detalles(request):
    return render(request,'core/detalles.html')

def equipo(request):
    return render(request,'core/equipo.html')

def servicio(request):
    return render(request,'core/servicio.html')

def sobrenosotros(request):
    return render(request,'core/sobrenosotros.html')

def testimonios(request):
    return render(request,'core/testimonios.html')

def logeado(request):
    return render(request,'core/logeado.html')