# Generated by Django 5.0.7 on 2024-09-23 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requisicao', '0013_delete_requisicoescrate'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='estoque_antenista',
            unique_together=set(),
        ),
    ]
