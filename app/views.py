from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def crear_usuario(request):
    prueba_usuario_1 = usuario(id= 1, nombre="Pepe", apellidos="Perez", password="1234", email="prueba1@gmail.com", tipo=2, img="https://www.google.com", fecha_nacimiento="1999-01-01", sexo="Hombre")
    prueba_usuario_1.save()
    prueba_usuario_2 = usuario(id= 2,nombre="Juan", apellidos="Garcia", password="1234", email="prueba2@gmai.com", tipo=2, img="https://www.google.com", fecha_nacimiento="1999-01-01", sexo="Hombre")
    prueba_usuario_2.save()
    prueba_usuario_3 = usuario(id= 3,nombre="Maria", apellidos="Lopez", password="1234", email="prueba3@gmail.com", tipo=2, img="https://www.google.com", fecha_nacimiento="1999-01-01", sexo="Mujer")
    prueba_usuario_3.save()
    return HttpResponse("Usuario creado")

def crear_pelicula(request):
    pelicula_1 = pelicula(id=1, nombre="Harry Potter", sinopsis="Magia", fecha_estreno="2001-01-01", img="https://www.google.com", url_trailer="https://www.google.com", director="Desconocido")
    pelicula_1.save()
    pelicula_2 = pelicula(id=2, nombre="Harry Potter 2", sinopsis="Magia", fecha_estreno="2002-01-01", img="https://www.google.com", url_trailer="https://www.google.com", director="Desconocido")
    pelicula_2.save()
    pelicula_3 = pelicula(id=3, nombre="Harry Potter 3", sinopsis="Magia", fecha_estreno="2003-01-01", img="https://www.google.com", url_trailer="https://www.google.com", director="Desconocido")
    pelicula_3.save()
    return HttpResponse("Pelicula creada")
def crear_genero(request):
    genero_1 = genero(id=1, nombre="Terror", descripcion="Miedo")
    genero_1.save()
    genero_2 = genero(id=2, nombre="Comedia", descripcion="Risas")
    genero_2.save()
    genero_3 = genero(id=3, nombre="Accion", descripcion="Peleas")
    genero_3.save()
    return HttpResponse("Genero creado")

def crear_actor(request):
    actor_1 = actor(id=1, nombre="Angelina Jolie", img="https://www.google.com")
    actor_1.save()
    actor_2 = actor(id=2, nombre="Brad Pitt", img="https://www.google.com")
    actor_2.save()
    actor_3 = actor(id=3, nombre="Tom Cruise", img="https://www.google.com")
    actor_3.save()
    return HttpResponse("Actor creado")
