# Generated by Django 3.2.9 on 2021-11-19 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0003_alter_anuncio_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anuncio',
            name='preco',
        ),
    ]
