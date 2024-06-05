from django.db import models

# Create your models here.

class Dogs(models.Model):

    Name=models.CharField(max_length=40)
    Race=models.CharField(max_length=40)
    Gender=models.CharField(max_length=40)
    Age=models.CharField(max_length=40) #Lo puse como texto porque la idea es que puedas poner si tiene por ejemplo 2 meses o 2 años y no tener que andar haciendo calculos ponendiendo que tiene X cantidad de meses.


class Cats(models.Model):

    Name=models.CharField(max_length=40)
    Race=models.CharField(max_length=40)
    Gender=models.CharField(max_length=40)
    Age=models.CharField(max_length=40)


class Adopted_Pet(models.Model):

    User_Name=models.CharField(max_length=40)
    User_Lastname=models.CharField(max_length=40)
    User_Adress=models.CharField(max_length=100)
    Celphone_Number=models.IntegerField() #Este si lo puse como Int porque solo pondrán un numero de telefono.
    Pet_Name=models.CharField(max_length=40)
    Pet_Race=models.CharField(max_length=40)