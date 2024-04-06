"""
URL configuration for ONLYWATCH project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crear_usuario/', views.crear_usuario),
    path('crear_pelicula/', views.crear_pelicula),
    path('crear_genero/', views.crear_genero),
    path('crear_actor/', views.crear_actor),
    path('crear_serie/', views.crear_serie),
    path('crear_plataforma/', views.crear_plataforma),
    path('crear_foro_serie/', views.crear_foro_serie),

    path('crear_foro_pelicula/', views.crear_foro_pelicula),
    path('crear_comentario_serie/', views.crear_comentario_serie),
    path('crear_comentario_pelicula/', views.crear_comentario_pelicula),
    path('crear_respuestas_series/', views.crear_respuestas_series),
    path('crear_respuestas_peliculas/', views.crear_respuestas_peliculas),
    path('crear_temporada/', views.crear_temporada),
    path('crear_capitulo/', views.crear_capitulo),
    path('crear_valoracion_serie/', views.crear_valoracion_serie),
    path('crear_valoracion_pelicula/', views.crear_valoracion_pelicula),
    path('crear_pelicula_favorita/', views.crear_pelicula_favorita),
    path('crear_serie_favorita/', views.crear_serie_favorita),
    path('crear_plataforma_pelicula/', views.crear_plataforma_pelicula),
    path('crear_plataforma_serie/', views.crear_plataforma_series),
    path('crear_personaje_pelicula/', views.crear_personaje_pelicula),
    path('crear_personaje_serie/', views.crear_personaje_series),
    path('crear_pelicula_genero/', views.crear_pelicula_genero),
    path('crear_serie_genero/', views.crear_serie_genero),




]

