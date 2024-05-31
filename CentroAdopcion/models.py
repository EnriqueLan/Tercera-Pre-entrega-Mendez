from django.db import models

# Create your models here.

class Perros(models.Model):

    Nombre=models.CharField(max_length=40)
    Raza=models.CharField(max_length=40)
    Genero=models.CharField(max_length=40)
    Edad_Meses=models.IntegerField()


class Gatos(models.Model):

    Nombre=models.CharField(max_length=40)
    Raza=models.CharField(max_length=40)
    Genero=models.CharField(max_length=40)
    Edad_Meses=models.IntegerField()


class Mascota_Adoptada(models.Model):

    NombrePersona=models.CharField(max_length=40)
    ApellidoPersona=models.CharField(max_length=40)
    DireccionPersona=models.CharField(max_length=100)
    NumeroPersona=models.IntegerField()
    NombreMascota=models.CharField(max_length=40)
    EspecieMascota=models.CharField(max_length=40)