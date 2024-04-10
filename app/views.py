import os
from django.core.files import File
from .models import *
from django.http import HttpResponse
from django.db import connection
from templates import *


# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

def mostrar_admi(request):
    return render(request, 'admi.html')

def mostrar_peliculas(request):
    peliculas = pelicula.objects.all()
    return render(request, 'admi.html', {'peliculas': peliculas})


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        nombre_completo = request.POST.get('nombre_completo')
        mail = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        errors = []

        if password != password2:
            errors.append("Las contraseñas no coinciden")
        existe_usuario = Usuario.objects.filter(username=username).exists()
        if existe_usuario:
            errors.append("Ya existe un usuario con ese nombre")
        existe_mail = Usuario.objects.filter(email=mail).exists()
        if existe_mail:
            errors.append("Ya existe un usuario con ese email")

        if len(errors) != 0:
            return render(request, "register.html", {"errores": errors, "username": username})
        else:
            user = Usuario.objects.create_user(username=username, email=mail, password=password, nombre_completo=nombre_completo)
            user.save()
            return redirect("login.html")


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