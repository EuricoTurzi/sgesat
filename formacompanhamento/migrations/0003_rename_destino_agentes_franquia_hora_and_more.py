# Generated by Django 5.1.1 on 2024-09-26 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formacompanhamento', '0002_agentes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agentes',
            old_name='destino',
            new_name='franquia_hora',
        ),
        migrations.RenameField(
            model_name='agentes',
            old_name='origen',
            new_name='franquia_km',
        ),
    ]
