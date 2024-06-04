from django.shortcuts import render, redirect
from .models import Perros, Gatos, Mascota_Adoptada
from .forms import PerroFormulario, GatoFormulario, MascotaAdoptadaFormulario, BuscarFormulario

def home(request):
    return render(request, 'home.html')

def agregar_perro(request):
    if request.method == "POST":
        form = PerroFormulario(request.POST)
        if form.is_valid():
            Perros.objects.create(
                Nombre=form.cleaned_data['Nombre'],
                Raza=form.cleaned_data['Raza'],
                Genero=form.cleaned_data['Genero'],
                Edad_Meses=form.cleaned_data['Edad_Meses']
            )
            return redirect('home')
    else:
        form = PerroFormulario()
    return render(request, 'agregar_perro.html', {'form': form})

def buscar_mascota(request):
    if request.method == "POST":
        form = BuscarFormulario(request.POST)
        if form.is_valid():
            especie = form.cleaned_data['especie']
            nombre = form.cleaned_data['nombre']
            if especie == 'Perro':
                resultados = Perros.objects.filter(Nombre__icontains=nombre)
            else:
                resultados = Gatos.objects.filter(Nombre__icontains=nombre)
            return render(request, 'resultados.html', {'resultados': resultados})
    else:
        form = BuscarFormulario()
    return render(request, 'buscar_mascota.html', {'form': form})