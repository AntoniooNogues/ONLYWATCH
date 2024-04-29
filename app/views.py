from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
import os
from django.conf import settings
from django.shortcuts import render, redirect
from .models import *

import json

def mostrar_admi(request):
    return render(request, 'admi.html')

def mostrar_peliculas(request):
    peliculas = pelicula.objects.all()
    return render(request, 'admi.html', {'peliculas': peliculas})
def do_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            # Redirección tras un login exitoso
            return redirect('home')
        else:
            # Mensaje de error si la autenticación falla
            return render(request, 'login.html', {"error": "No se ha podido iniciar sesión intentalo de nuevo"})

    # Mostrar formulario de login para método GET
    return render(request, 'login.html')
def do_logout(request):
    logout(request)
    return redirect('login')
def mostrar_inicio(request):
    "add_peliculas_json()"
    "add_series_json()"
    headerP = list(pelicula.objects.all()[:5])
    headerS = list(serie.objects.all()[:5])
    headerPS = headerP + headerS
    series = list(serie.objects.all())
    peliculas = list(pelicula.objects.all())
    PyS = series + peliculas
    return render(request, 'user_home.html', {'header': headerPS, 'peliyserie': PyS})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        nombre_completo = request.POST.get('nombre_completo')
        mail = request.POST.get('email')
        password = request.POST.get('password1')
        password_confirmacion = request.POST.get('password2')

        errors = []

        if password != password_confirmacion:
            errors.append("Las contraseñas no coinciden")
        existe_usuario = User.objects.filter(username=username).exists()
        if existe_usuario:
            errors.append("Ya existe un usuario con ese nombre")
        existe_mail = User.objects.filter(email=mail).exists()
        if existe_mail:
            errors.append("Ya existe un usuario con ese email")

        if len(errors) != 0:
            return render(request, "register.html", {"errores": errors, "username": username})
        else:
            user = User.objects.create(username=username, email=mail, password=make_password(password), nombre_completo=nombre_completo)
            user.save()
            return redirect("login")


def reset_password(request):
    if request.method == 'GET':
        return render(request, 'reset_password.html')
    else:
        return render(request, 'reset_password.html')

def new_peliculas(request):
    if request.method == 'GET':
        uno = pelicula.objects.all()
        return render(request, 'admi.html', {'peliculas': uno})
    else:
        new = pelicula()
        new.nombre = request.POST.get('nombre')
        new.sinopsis = request.POST.get('sinopsis')
        new.fecha_estreno = request.POST.get('fecha_estreno')
        new.img = request.POST.get('img')
        new.url_trailer = request.POST.get('url_trailer')
        new.director = request.POST.get('director')
        new.save()

        return redirect('/administrador/pelicula')

def new_serie(request):
    if request.method == 'GET':
        uno = serie.objects.all()
        return render(request, 'admi.html', {'serie': uno})
    else:
        new = serie()
        new.nombre = request.POST.get('nombre_serie')
        new.sinopsis = request.POST.get('sinopsis_serie')
        new.fecha_estreno = request.POST.get('fecha_estreno_serie')
        new.img = request.POST.get('img_serie')
        new.trailer = request.POST.get('trailer_serie')
        new.director = request.POST.get('director_serie')
        new.save()

        return redirect('/administrador/serie')
def mostrar_series(request):
    series = serie.objects.all()
    return render(request, 'admi.html', {'series': series})

def mostrar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'admi.html', {'usuarios': usuarios})

def eliminar_usuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect('/administrador/')

def eliminar_pelicula(request, id):
    pelicula_eliminar = pelicula.objects.get(id=id)
    pelicula_eliminar.delete()
    return redirect('/administrador/')

def eliminar_serie(request, id):
    serie_eliminar = serie.objects.get(id=id)
    serie_eliminar.delete()
    return redirect('/administrador/')
def editar_pelicula(request, id):
    peli = pelicula.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'editar_pelicula.html', {'pelicula': peli})
    else:
        peli.nombre = request.POST.get('nombre')
        peli.sinopsis = request.POST.get('sinopsis')
        peli.fecha_estreno = request.POST.get('fecha_estreno')
        peli.img = request.POST.get('img')
        peli.url_trailer = request.POST.get('url_trailer')
        peli.director = request.POST.get('director')
        peli.save()

        return redirect('/administrador/')

def editar_serie(request, id):
    serie_editar = serie.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'editar_serie.html', {'serie': serie_editar})
    else:
        serie_editar.nombre = request.POST.get('nombre')
        serie_editar.sinopsis = request.POST.get('sinopsis')
        serie_editar.fecha_estreno = request.POST.get('fecha_estreno')
        serie_editar.img = request.POST.get('img')
        serie_editar.url_trailer = request.POST.get('trailer')
        serie_editar.director = request.POST.get('director')
        serie_editar.save()

        return redirect('/administrador/')

def configuracion(request):
    usuario = request.user.username
    if usuario is not None:
        user = User.objects.get(username=usuario)
        return render(request, 'User_information.html', {'user': user})
    else:
        return render(request, 'login.html')

def plataformas(request):
    add_plataformas()
    plt = plataforma.objects.all()
    return render(request, 'plataformas.html', {'plataforma': plt})


def add_plataformas():
    # Directory where the images are located
    directory = os.path.join(settings.MEDIA_ROOT, 'plataformas')    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            # Get the file name without the extension
            name = os.path.splitext(filename)[0]
            # Construct the relative path by adding 'plataformas'
            relative_path = os.path.join('plataformas', filename)
            # Check if the name already exists in the database to avoid duplicates
            if not plataforma.objects.filter(nombre=name).exists():
                # Create a new instance of the model with the desired path
                new_plataforma = plataforma(nombre=name, img=relative_path)
                new_plataforma.save()

def add_peliculas_json():
    with open('static/Peliculas.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Itera sobre cada elemento en los datos
    for item in data:
        # Crea una nueva instancia del modelo pelicula
        new_pelicula = pelicula()
        # Asigna los valores de los campos
        new_pelicula.nombre = item['nombre']
        new_pelicula.sinopsis = item['sinopsis']
        new_pelicula.anyo_estreno = item['anyo_estreno']
        new_pelicula.director = item['director']
        # Asigna las URLs de la imagen y el tráiler
        new_pelicula.img = item['img']
        new_pelicula.trailer = item['trailer']
        new_pelicula.save()

def add_series_json():
    with open('static/Series.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Itera sobre cada elemento en los datos
    for item in data:
        # Crea una nueva instancia del modelo pelicula
        new_serie = serie()
        # Asigna los valores de los campos
        new_serie.nombre = item['nombre']
        new_serie.sinopsis = item['sinopsis']
        new_serie.anyo_estreno = item['anyo_estreno']
        new_serie.director = item['director']
        # Asigna las URLs de la imagen y el tráiler
        new_serie.img = item['img']
        new_serie.trailer = item['trailer']
        new_serie.save()