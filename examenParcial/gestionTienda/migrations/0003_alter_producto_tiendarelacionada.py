# Generated by Django 4.2.3 on 2023-07-29 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionTienda', '0002_alter_producto_cantidad_alter_producto_precioventa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='tiendaRelacionada',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestionTienda.tienda'),
        ),
    ]
