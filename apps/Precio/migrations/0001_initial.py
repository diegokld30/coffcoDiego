# Generated by Django 5.0.4 on 2024-08-17 03:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('TipoServicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado_precio', models.CharField(max_length=45)),
                ('presentacion', models.CharField(max_length=45)),
                ('precio', models.FloatField()),
                ('tiposervicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TipoServicio.tiposervicio')),
            ],
        ),
    ]
