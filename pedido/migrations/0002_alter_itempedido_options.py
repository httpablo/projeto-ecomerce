# Generated by Django 5.1.1 on 2024-09-30 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itempedido',
            options={'verbose_name': 'Item do pedido', 'verbose_name_plural': 'Itens do pedido'},
        ),
    ]