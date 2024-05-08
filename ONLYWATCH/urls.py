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
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # path('', views.cargar_datos_sql, name='cargar_datos_sql'),
    # Acceso de Usuario/No Usuario a Login, Registro, Logout y Reinicio de Contraseña
    path('login/', views.do_login, name='login'),
    path('logout/', views.do_logout, name='logout'),
    path('register/', views.register, name='signup'),
    path('login/reset_password', views.reset_password, name='reset_password'),


    # Administracion de la Aplicacion
    path('inicio_admi/', views.mostrar_admi),
    path('administrador/', views.mostrar_peliculas, name='admi'),
    path('administrador/pelicula', views.new_peliculas, name='new_peliculas'),
    path('administrador/serie', views.new_serie, name='new_series'),
    path('administrador/', views.mostrar_admi, name='inicio_admi'),
    path('administrador/peliculas_actuales', views.mostrar_peliculas, name='mostrarPeliculas'),
    path('administrador/new_pelicula', views.new_peliculas, name='new_peliculas'),
    path('administrador/new_serie', views.new_serie, name='new_series'),
    path('administrador/series_actuales', views.mostrar_series, name='mostrar_series'),
    path('administrador/usuarios_actuales', views.mostrar_usuarios, name='mostrar_usuarios'),
    path('administrador/eliminar_usuario/<int:id>', views.eliminar_usuario, name='eliminar_usuario'),
    path('administrador/eliminar_pelicula/<int:id>', views.eliminar_pelicula, name='eliminar_pelicula'),
    path('administrador/eliminar_serie/<int:id>', views.eliminar_serie, name='eliminar_serie'),
    path('administrador/editar_pelicula/<int:id>', views.editar_pelicula, name='editar_pelicula'),
    path('administrador/editar_serie/<int:id>', views.editar_serie, name='editar_serie'),
    path('administrador/actores', views.new_actor, name='new_actor'),
    path('administrador/listado_actores', views.mostrar_actores, name='mostrar_actores'),
    path('administrador/eliminar_actor/<int:id>', views.eliminar_actor, name='eliminar_actor'),
    path('administrador/editar_actor/<int:id>', views.editar_actor, name='editar_actor'),


    # Paginas de la Aplicacion Peliculas/Series
    path('home/', views.mostrar_inicio, name='home'),
    path('peliculas/', views.view_peliculas, name='peliculas'),
    path('plataformas/', views.plataformas, name='plataformas'),
    path('series/', views.view_series, name='series'),
    path('pelicula/<int:id_pelicula>', views.mostrar_pelicula, name='pelicula'),
    path('pelicula/valorar/<int:id_pelicula>', views.valorar_pelicula, name='valorar_pelicula'),
    path('pelicula_favorita/<int:id_pelicula>/', views.pelicula_favorita, name='pelicula_favorita'),

    # Paginas de configuracion de Usuario
    path('usuario/perfil', views.configuracion, name='configuracion'),
    path('send_verification_code/', views.send_verification_code, name='send_verification_code'),
    path('verify_code/', views.verify_code, name='verify_code'),
    path('vincular_desvincular_plataforma/<int:plataforma_id>/', views.vincular_desvincular_plataforma, name='vincular_desvincular_plataforma'),
    path('editar_perfil/', views.configurar_perfil, name='editar_perfil'),
    path('load_series_data/', views.load_series_data, name='load_series_data'),
    path('load_movies_data/', views.load_movies_data, name='load_movies_data'),
    path('administrador/new_actores', views.new_actor, name='new_actor'),
    path('administrador/listado_actores', views.mostrar_actores, name='mostrar_actores'),
    path('administrador/eliminar_actor/<int:id>', views.eliminar_actor, name='eliminar_actor'),
    path('administrador/editar_actor/<int:id>', views.editar_actor, name='editar_actor'),
    path('administrador/pelicula/vincular_pelicula/<int:id>', views.add_uniones_peliculas, name='vincular_pelicula'),
    path('administrador/listado_generos', views.mostrar_generos, name='mostrar_generos'),
    path('administrador/new_genero', views.new_genero, name='new_genero'),
    path('administrador/editar_genero/<int:id>', views.editar_genero, name='editar_genero'),
    path('administrador/pelicula/vincular_pelicula/vincular_genero/<int:id>/', views.vincular_desvincular_genero_pelicula, name='toggle_genre'),
    path('administrador/pelicula/vincular_pelicula/vincular_plataforma/<int:id>/', views.vincular_desvincular_plataforma_pelicula, name='plataforma_pelicula'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

