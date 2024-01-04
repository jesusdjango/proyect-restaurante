# Generated by Django 4.2.7 on 2024-01-03 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_pedido_delete_plate'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Total Precio'),
        ),
    ]