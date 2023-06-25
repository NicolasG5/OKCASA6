# Generated by Django 4.1.9 on 2023-06-04 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_tecnico_solicitudenlinea'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='solicitudenlinea',
            name='tecnico',
        ),
        migrations.AddField(
            model_name='solicitudenlinea',
            name='tecnico_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.tecnico'),
        ),
    ]
