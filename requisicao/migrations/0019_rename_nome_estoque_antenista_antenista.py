# Generated by Django 5.1.1 on 2024-09-25 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requisicao', '0018_rename_antenista_estoque_antenista_nome'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estoque_antenista',
            old_name='nome',
            new_name='antenista',
        ),
    ]
