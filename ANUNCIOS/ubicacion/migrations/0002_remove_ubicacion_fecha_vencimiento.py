# Generated by Django 3.2.9 on 2021-11-19 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ubicacion', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ubicacion',
            name='fecha_vencimiento',
        ),
    ]
