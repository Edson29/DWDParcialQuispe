from django.urls import path
from . import views

app_name = 'gestionTienda'

urlpatterns = [
    path('', views.index, name='index'),
    path('Productos', views.productos, name='productos'),
    path('Tiendas',views.tiendas, name='tiendas'),
    path('Detalle/<idTienda>', views.detalle, name="detalle"),
    path('EliminarProducto/<idProducto>', views.eliminarProducto, name='eliminarProducto'),
    path('AgregarProducto/<idTienda>', views.agregarProducto, name='agregarProducto')

]