from django.urls import path

from CentroAdopcion import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar_perro/', views.agregar_perro, name='agregar_perro'),
    path('buscar_mascota/', views.buscar_mascota, name='buscar_mascota'),
]