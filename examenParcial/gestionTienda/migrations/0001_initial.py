# Generated by Django 4.2.3 on 2023-07-28 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tienda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(blank=True, max_length=50, null=True)),
                ('provincia', models.CharField(blank=True, max_length=50, null=True)),
                ('region', models.CharField(blank=True, max_length=50, null=True)),
                ('fechaCreacion', models.DateField(blank=True, max_length=50, null=True)),
                ('telefono', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('codigo', models.CharField(blank=True, max_length=50, null=True)),
                ('precioVenta', models.CharField(blank=True, max_length=50, null=True)),
                ('cantidad', models.CharField(blank=True, max_length=50, null=True)),
                ('tiendaRelacionada', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestionTienda.tienda')),
            ],
        ),
    ]
