# Generated by Django 5.0.4 on 2024-08-17 03:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Municipio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Finca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_finca', models.CharField(max_length=50)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Municipio.municipio')),
            ],
        ),
    ]
