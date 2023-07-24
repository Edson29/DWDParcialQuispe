from django.urls import path
from . import views

app_name = 'gestionTienda'

urlpatterns = [
    path('', views.index, name='index'),
    path('Productos', views.productos, name='productos'),
    path('Tiendas',views.tiendas, name='tiendas'),
    path('Detalle-tiendas', views.detalle, name="detalle")

]