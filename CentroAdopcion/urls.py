from django.urls import path

from CentroAdopcion import views

urlpatterns = [
    path('', views.inicio),
]