# Generated by Django 4.1.9 on 2023-06-05 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_remove_solicitudenlinea_servicios_solicitudservicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudenlinea',
            name='estado',
            field=models.CharField(default='Pendiente', max_length=100),
        ),
    ]
