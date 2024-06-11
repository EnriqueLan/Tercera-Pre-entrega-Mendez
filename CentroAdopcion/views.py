from django.shortcuts import render
from .models import *
from .forms import *

def home(req):
    return render(req, 'home.html')

def Dogs_List(req):

  list = Dogs.objects.all()

  return render(req, "lista_Perros.html", {"lista_Perros": list})

def Cats_List(req):

  list = Cats.objects.all()

  return render(req, "lista_Gatos.html", {"lista_Gatos": list})

def Add_New_Dog(req):
    if req.method == "POST":
        form = DogsForm(req.POST)
        if form.is_valid():
            Dogs.objects.create(
                Name=form.cleaned_data['Name'],
                Race=form.cleaned_data['Race'],
                Gender=form.cleaned_data['Gender'],
                Age=form.cleaned_data['Age']
            )
            return render(req,'home.html')
    else:
        form = DogsForm()
    return render(req, 'agregar_perro.html', {'form': form})

def Add_New_Cat(req):
    if req.method == "POST":
        form = CatsForm(req.POST)
        if form.is_valid():
            Cats.objects.create(
                Name=form.cleaned_data['Name'],
                Race=form.cleaned_data['Race'],
                Gender=form.cleaned_data['Gender'],
                Age=form.cleaned_data['Age']
            )
            return render(req,'home.html')
    else:
        form = CatsForm()
    return render(req, 'agregar_gato.html', {'form': form})

def Adopt_Pet(req):
    if req.method == "POST":
        form = Pet_to_AdoptForm(req.POST)
        if form.is_valid():
            Adopted_Pet.objects.create(
                User_Name=form.cleaned_data['UserName'],
                User_Lastname=form.cleaned_data['UserLastname'],
                User_Adress=form.cleaned_data['UserAdress'],
                Celphone_Number=form.cleaned_data['CelphoneNumber'],
                Pet_Name=form.cleaned_data['PetName'],
                Pet_Race=form.cleaned_data['PetRace']
            )
            return render(req,'home.html')
    else:
        form = Pet_to_AdoptForm()
    return render(req, 'adoptar_mascota.html', {'form': form})

def Search_Pet(req):
    if req.method == "POST":
        form = SearchForm(req.POST)
        if form.is_valid():
            species = form.cleaned_data['Race']
            Name = form.cleaned_data['Name']
            if species == 'Perro':
                resultados = Dogs.objects.filter(Name__icontains=Name)
            else:
                resultados = Cats.objects.filter(Name__icontains=Name)
            return render(req, 'resultados.html', {'resultados': resultados})
    else:
        form = SearchForm()
    return render(req, 'buscar_mascota.html', {'form': form})
