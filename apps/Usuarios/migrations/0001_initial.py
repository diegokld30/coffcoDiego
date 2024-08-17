# Generated by Django 5.0.4 on 2024-08-17 03:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Rol', '0001_initial'),
        ('tipoDocumento', '0002_delete_ambiente_remove_documentos_logos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('apellidos', models.CharField(max_length=45)),
                ('correo_electronico', models.EmailField(max_length=100)),
                ('contrasena', models.CharField(max_length=45)),
                ('numero_documento', models.IntegerField()),
                ('estado', models.BooleanField()),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Rol.rol')),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipoDocumento.tipodocumento')),
            ],
        ),
    ]
