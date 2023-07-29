from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Tienda, Producto
from datetime import date

# Create your views here.

def index(request):    
    return HttpResponseRedirect(reverse('gestionTienda:tiendas'))

def productos(request):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        codigo = request.POST.get('codigo')
        precioVenta = request.POST.get('precioVenta')
        cantidad = request.POST.get('cantidad')
        idTienda = request.POST.get('tienda')
        tienda = Tienda.objects.get(id=idTienda)
        Producto.objects.create(
            descripcion = descripcion,
            codigo = codigo,
            precioVenta = precioVenta,
            cantidad = cantidad,
            tiendaRelacionada = tienda
        )
        return HttpResponseRedirect(reverse('gestionTienda:productos'))

    return render(request, 'productos.html', {
        'listaProductos': Producto.objects.all().order_by('id'),
        'listaTiendas': Tienda.objects.all().order_by('id')
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
        'tienda': tienda.provincia + ' - ' + tienda.region,
        'idTienda':idTienda
    })

def eliminarProducto(request, idProducto):
    producto = Producto.objects.get(id=idProducto)
    tienda = producto.tiendaRelacionada
    idTienda = tienda.id
    producto.delete()
    return HttpResponseRedirect(reverse('gestionTienda:detalle',kwargs={'idTienda':idTienda}))

def agregarProducto(request, idTienda):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        codigo = request.POST.get('codigo')
        precioVenta = request.POST.get('precioVenta')
        cantidad = request.POST.get('cantidad')
        #idTienda = request.POST.get('tienda')
        tienda = Tienda.objects.get(id=idTienda)
        Producto.objects.create(
            descripcion = descripcion,
            codigo = codigo,
            precioVenta = precioVenta,
            cantidad = cantidad,
            tiendaRelacionada = tienda
        )
        return HttpResponseRedirect(reverse('gestionTienda:detalle',kwargs={'idTienda':idTienda}))




    
        
