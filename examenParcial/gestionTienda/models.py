from django.db import models

# Create your models here.
class Tienda(models.Model):
    direccion = models.CharField(max_length=50, blank=True, null=True)
    provincia = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    fechaCreacion = models.DateField( blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)


class Producto(models.Model):
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    precioVenta = models.FloatField(blank=True, null=True)
    cantidad = models.IntegerField(blank=True, null=True)
    tiendaRelacionada = models.ForeignKey(Tienda, on_delete=models.SET_NULL, blank=True, null=True)
