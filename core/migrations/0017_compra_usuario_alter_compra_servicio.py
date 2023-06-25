# Generated by Django 4.1.9 on 2023-06-20 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0016_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='compra',
            name='servicio',
            field=models.CharField(max_length=255),
        ),
    ]
