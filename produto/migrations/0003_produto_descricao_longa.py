# Generated by Django 5.1.1 on 2024-09-30 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_alter_produto_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='descricao_longa',
            field=models.TextField(default=''),
        ),
    ]
