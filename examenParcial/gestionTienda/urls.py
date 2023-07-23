from django.urls import path
from . import views

app_name = 'gestionTienda'

urlpatterns = [
    path('', views.index, name='index'),
    path('productos', views.productos, name='productos'),
    path('tiendas',views.tiendas, name='tiendas'),
    path('detalle-tiendas', views.detalle, name="detalle")

]