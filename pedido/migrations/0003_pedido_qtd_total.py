# Generated by Django 5.1.1 on 2024-10-09 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_alter_itempedido_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='qtd_total',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
