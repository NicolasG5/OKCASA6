# Generated by Django 4.1.9 on 2023-06-04 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_solicitudenlinea_apellido_solicitudenlinea_correo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudenlinea',
            name='apellido',
            field=models.CharField(default='{{ solicitud.apellido }}', max_length=100),
        ),
    ]
