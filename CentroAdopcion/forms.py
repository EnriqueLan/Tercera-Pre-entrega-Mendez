from django import forms

class DogsForm(forms.Form):
    Name = forms.CharField(max_length=40, label="Nombre del Perro:")
    Race = forms.CharField(max_length=40, label="Raza:")
    Gender = forms.CharField(max_length=40, label="Genero:(Macho o Hembra)")
    Age = forms.CharField(max_length=40, label="Escriba la edad que tiene:(especifique si son años o meses)") #Lo mismo que con la edad de los modelos, para no hacer tanto lio haciendo calculos el usuario puede poner como texto si son X años o X meses de vida.

class CatsForm(forms.Form):
    Name = forms.CharField(max_length=40, label="Nombre del Gato:")
    Race = forms.CharField(max_length=40, label="Raza:")
    Gender = forms.CharField(max_length=40, label="Genero:(Macho o Hembra)")
    Age = forms.CharField(max_length=40, label="Escriba la edad que tiene:(especifique si son años o meses)")


class SearchForm(forms.Form):
    Breeds = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    ]
    Race = forms.ChoiceField(choices=Breeds, label="Seleccione la Especie de la Mascota que quiere Buscar:")
    Name = forms.CharField(max_length=40, label="Díganos cómo se llama la Mascota que está buscando:")


class Pet_to_AdoptForm(forms.Form):
    NamePersona = forms.CharField(
        max_length=40, 
        label="Ingrese su Nombre por favor"
    )
    ApellidoPersona = forms.CharField(
        max_length=40, 
        label="Ingrese su Apellido por favor"
    )
    DireccionPersona = forms.CharField(
        max_length=100, 
        label="debe ingresar su Dirección por favor"
    )
    NumeroPersona = forms.IntegerField(
        label="Ingrese su Número de Teléfono tambien"
    )
    NameMascota = forms.CharField(
        max_length=40, 
        label="Como se llama la Mascota que desea adoptar"
    )
    EspecieMascota = forms.CharField(
        max_length=40, 
        label="Ingrese la Especie de su futura Mascota (Perro o Gato)"
    )