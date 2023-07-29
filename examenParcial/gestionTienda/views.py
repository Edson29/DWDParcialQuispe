from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Tienda, Producto
from datetime import date

# Create your views here.

def index(request):    
    return render(request, 'index.html')

def productos(request):    
    return render(request, 'productos.html', {
        'listaProductos': Producto.objects.all().order_by('id')
    })

def tiendas(request):
    if request.method=='POST':
        direccionTienda = request.POST.get('direccionTienda')
        provinciaTienda = request.POST.get('provinciaTienda')        
        regionTienda = request.POST.get('regionTienda')
        fechaCreacion = date.today()
        telefonoTienda = request.POST.get('telefonoTienda')
        Tienda.objects.create(
            direccion = direccionTienda,
            provincia = provinciaTienda,
            region = regionTienda,
            fechaCreacion = fechaCreacion,
            telefono = telefonoTienda,
        )
        return HttpResponseRedirect(reverse('gestionTienda:tiendas'))    
    return render(request, 'tiendas.html', {
        'listaTiendas': Tienda.objects.all().order_by('id')
    })

def detalle(request, idTienda):   
    tienda = Tienda.objects.get(id=idTienda)
    listaProductosTienda = Producto.objects.all().filter(tiendaRelacionada = tienda)
    return render(request, 'detalle.html',{
        'productosTienda': listaProductosTienda,
        'tienda': tienda.provincia
    })


    
        
