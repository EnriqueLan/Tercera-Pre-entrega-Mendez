from django.urls import path

from CentroAdopcion import views

urlpatterns = [
    path('', views.home, name='home'),
    path('agregar_perro/', views.Add_New_Dog, name='agregar_perro'),
    path('agregar_gato/', views.Add_New_Cat, name='agregar_gato'),
    path('buscar_mascota/', views.Search_Pet, name='buscar_mascota'),
    path('adoptar_mascota/', views.Adopt_Pet, name='adoptar_mascota'),
    path('Lista_Perros/', views.Dogs_List, name='Lista_Perros'),
    path('Lista_Gatos/', views.Cats_List, name='Lista_Gatos')
]