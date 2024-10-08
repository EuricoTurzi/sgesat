# Generated by Django 5.0.7 on 2024-09-12 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=255)),
                ('cnpj', models.CharField(max_length=50)),
                ('inicio_de_contrato', models.CharField(max_length=14)),
                ('vigencia', models.CharField(blank=True, choices=[('', ''), ('12', '12'), ('24', '24'), ('36', '36'), ('48', '48')], max_length=50, null=True)),
                ('termino', models.CharField(blank=True, max_length=10, null=True)),
                ('equipamento', models.CharField(choices=[('Isaca', 'Isca'), ('Rastreador', 'Rastreador'), ('Tets', 'Tets')], max_length=50, null=True)),
                ('quantidade', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
