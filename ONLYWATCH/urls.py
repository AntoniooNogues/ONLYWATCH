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
    path('login/', views.login, name='login'),
    path('register/', views.register, name='signup'),
    path('login/reset_password', views.reset_password, name='reset_password'),

    path('', views.mostrar_admi),
    path('administrador/', views.mostrar_peliculas, name='admi'),
    path('administrador/pelicula', views.new_peliculas, name='new_peliculas'),
    path('administrador/serie', views.new_serie, name='new_series'),
    path('administrador/series_actuales', views.mostrar_series, name='mostrar_series'),
    path('administrador/usuarios', views.mostrar_usuarios, name='mostrar_usuarios'),
    path('administrador/eliminar_usuario/<int:id>', views.eliminar_usuario, name='eliminar_usuario'),
    path('administrador/eliminar_pelicula/<int:id>', views.eliminar_pelicula, name='eliminar_pelicula'),
    path('administrador/eliminar_serie/<int:id>', views.eliminar_serie, name='eliminar_serie'),
    path('administrador/editar_pelicula/<int:id>', views.editar_pelicula, name='editar_pelicula'),
    path('administrador/editar_serie/<int:id>', views.editar_serie, name='editar_serie'),
    path('usuario/perfil', views.settings, name='configuracion'),

]

