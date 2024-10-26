# Generated by Django 5.1.1 on 2024-10-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0009_alter_variacao_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='descricao_longa',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(default=0, verbose_name='Preço Promo.'),
        ),
    ]
