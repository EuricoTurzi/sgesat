# Generated by Django 5.1.1 on 2024-09-18 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t42', '0007_t42model_estoque_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='t42model',
            name='equipamento',
            field=models.CharField(choices=[('TETS', 'TETS'), ('TETS R', 'TETS R')], max_length=100, null=True),
        ),
    ]
