# Generated by Django 5.0.6 on 2024-05-30 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('Raza', models.CharField(max_length=40)),
                ('Genero', models.CharField(max_length=40)),
                ('Edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mascota_Adoptada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombrePersona', models.CharField(max_length=40)),
                ('ApellidoPersona', models.CharField(max_length=40)),
                ('DireccionPersona', models.CharField(max_length=100)),
                ('NumeroPersona', models.IntegerField()),
                ('NombreMascota', models.CharField(max_length=40)),
                ('EspecieMascota', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Perros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=40)),
                ('Raza', models.CharField(max_length=40)),
                ('Genero', models.CharField(max_length=40)),
                ('Edad', models.IntegerField()),
            ],
        ),
    ]
