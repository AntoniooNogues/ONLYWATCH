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

    # Acceso de Usuario/No Usuario a Login, Registro, Logout y Reinicio de Contraseña
    path('login/', views.do_login, name='login'),
    path('logout/', views.do_logout, name='logout'),
    path('registro', views.register, name='signup'),
    path('login/reset_password', views.reset_password, name='reset_password'),
    path('usuario/reset_password', views.cambiar_password, name='cambiar_password'),


    # Administracion de la Aplicacion
    path('administracion/', views.login_admi, name='administracion_login'),
    path('administracion/home/', views.mostrar_admi, name='administracion_home'),
    path('administracion/listado_peliculas', views.mostrar_peliculas, name='admiPeliculas'),
    path('administracion', views.new_peliculas, name='new_peliculas'),
    path('administracion/serie', views.new_serie, name='new_series'),
    path('administracion/', views.mostrar_admi, name='inicio_admi'),
    path('administracion/peliculas_actuales', views.mostrar_peliculas, name='mostrarPeliculas'),
    path('administracion/new_pelicula', views.new_peliculas, name='new_peliculas'),
    path('administracion/new_serie', views.new_serie, name='new_series'),
    path('administracion/series_actuales', views.mostrar_series, name='mostrar_series'),
    path('administracion/usuarios_actuales', views.mostrar_usuarios, name='mostrar_usuarios'),
    path('administracion/eliminar_usuario/<int:id>', views.eliminar_usuario, name='eliminar_usuario'),
    path('administracion/eliminar_pelicula/<int:id>', views.eliminar_pelicula, name='eliminar_pelicula'),
    path('administracion/eliminar_serie/<int:id>', views.eliminar_serie, name='eliminar_serie'),
    path('administracion/editar_pelicula/<int:id>', views.editar_pelicula, name='editar_pelicula'),
    path('administracion/editar_serie/<int:id>', views.editar_serie, name='editar_serie'),
    path('administracion/actores', views.new_actor, name='new_actor'),
    path('administracion/listado_actores', views.mostrar_actores, name='mostrar_actores'),
    path('administracion/eliminar_actor/<int:id>', views.eliminar_actor, name='eliminar_actor'),
    path('administracion/editar_actor/<int:id>', views.editar_actor, name='editar_actor'),
    path('administracion/new_actores', views.new_actor, name='new_actor'),
    path('administracion/listado_actores', views.mostrar_actores, name='mostrar_actores'),
    path('administracion/eliminar_actor/<int:id>', views.eliminar_actor, name='eliminar_actor'),
    path('administracion/editar_actor/<int:id>', views.editar_actor, name='editar_actor'),
    path('administracion/pelicula/vincular_pelicula/<int:id>', views.add_uniones_peliculas, name='vincular_pelicula'),
    path('administracion/listado_generos', views.mostrar_generos, name='mostrar_generos'),
    path('administracion/new_genero', views.new_genero, name='new_genero'),
    path('administracion/editar_genero/<int:id>', views.editar_genero, name='editar_genero'),
    path('administracion/pelicula/vincular_pelicula/vincular_genero/<int:id>/', views.vincular_desvincular_genero_pelicula, name='toggle_genre'),
    path('administracion/pelicula/vincular_pelicula/vincular_plataforma/<int:id>/', views.vincular_desvincular_plataforma_pelicula, name='plataforma_pelicula'),

    # Paginas de la Aplicacion Peliculas/Series
    path('', views.mostrar_inicio, name='home'),
    path('filtrar', views.filtrar, name='filtrar'),
    path('buscar/', views.buscar, name='buscar'),
    path('peliculas/', views.view_peliculas, name='peliculas'),
    path('peliculas/filtrar', views.filtrar_pelicula, name='filtrar_series'),
    path('plataformas/', views.plataformas, name='plataformas'),
    path('series/', views.view_series, name='series'),
    path('series/filtrar', views.filtrar_series, name='filtrar_series'),
    path('personal/', views.usuario_personal, name='personal'),
    path('pelicula/<int:id_pelicula>', views.mostrar_pelicula, name='pelicula'),
    path('pelicula/valorar/<int:id_pelicula>', views.valorar_pelicula, name='valorar_pelicula'),
    path('pelicula_favorita/<int:id_pelicula>/', views.pelicula_favorita, name='pelicula_favorita'),
    path('serie/<int:id_serie>', views.mostrar_serie, name='serie'),
    path('serie/valorar/', views.valorar_serie, name='valorar_serie'),
    path('serie_favorita/<int:id_serie>/', views.serie_favorita, name='serie_favorita'),
    path('pelicula/comentario', views.guardar_comentario, name='guardar_comentario'),
    path('serie/comentario', views.guardar_comentario_serie, name='guardar_comentario_serie'),

    # Paginas de configuracion de Usuario
    path('usuario/perfil', views.configuracion, name='configuracion'),
    path('send_verification_code/', views.send_verification_code, name='send_verification_code'),
    path('verify_code/', views.verify_code, name='verify_code'),
    path('plataformas/vincular_desvincular_plataforma/<int:plataforma_id>/', views.vincular_desvincular_plataforma, name='vincular_desvincular_plataforma'),
    path('editar_perfil/', views.configurar_perfil, name='editar_perfil'),

    # Cargar datos
    #path('cargar_datos_sql/', views.cargar_datos_sql, name='cargar_datos_sql'),
    # path('cargar_datos/actores/pelicula', views.anadir_actores_personaje_pelicula, name='cargar_datos_pelis_actores'),
    # path('cargar_datos/actores/serie', views.anadir_actores_personaje_serie, name='cargar_datos_series_actores'),
    # path('cargar_datos/anadir_base_datos/actores_personajes', views.cargar_actores_personajes, name='cargar_base_datos_actores_personajes'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

