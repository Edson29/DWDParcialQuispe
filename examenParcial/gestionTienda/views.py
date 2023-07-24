from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("Bienvenidos a la Aplicacion del Examen Parcial")
    return render(request, 'index.html')

def productos(request):
    #return HttpResponse("Vista de PRODUCTOS")
    return render(request, 'productos.html')

def tiendas(request):
    #return HttpResponse("Vista de TIENDAS")
    return render(request, 'tiendas.html')

def detalle(request):
    #return HttpResponse("Vista de detalle de TIENDAS")
    return render(request, 'detalle.html')