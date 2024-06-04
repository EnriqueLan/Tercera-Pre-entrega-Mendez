from django import forms

class PerroFormulario(forms.Form):
    Nombre = forms.CharField(max_length=40)
    Raza = forms.CharField(max_length=40)
    Genero = forms.CharField(max_length=40)
    Edad_Meses = forms.IntegerField()

class GatoFormulario(forms.Form):
    Nombre = forms.CharField(max_length=40)
    Raza = forms.CharField(max_length=40)
    Genero = forms.CharField(max_length=40)
    Edad_Meses = forms.IntegerField()

class MascotaAdoptadaFormulario(forms.Form):
    NombrePersona = forms.CharField(max_length=40)
    ApellidoPersona = forms.CharField(max_length=40)
    DireccionPersona = forms.CharField(max_length=100)
    NumeroPersona = forms.IntegerField()
    NombreMascota = forms.CharField(max_length=40)
    EspecieMascota = forms.CharField(max_length=40)

class BuscarFormulario(forms.Form):
    ESPECIES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    ]
    especie = forms.ChoiceField(choices=ESPECIES)
    nombre = forms.CharField(max_length=40)