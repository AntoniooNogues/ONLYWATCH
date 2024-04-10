from django.contrib.auth.hashers import make_password
import os
from django.core.files import File



# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

def crear_usuario(request):
    prueba_usuario_1 = Usuario(id= 1, nombre="Pepe", apellidos="Perez", password="1234", email="prueba1@gmail.com", tipo=2, img="https://www.google.com", fecha_nacimiento="1999-01-01", sexo="Hombre")
    prueba_usuario_1.save()
    prueba_usuario_2 = Usuario(id= 2,nombre="Juan", apellidos="Garcia", password="1234", email="prueba2@gmai.com", tipo=2, img="https://www.google.com", fecha_nacimiento="1999-01-01", sexo="Hombre")
    prueba_usuario_2.save()
    prueba_usuario_3 = Usuario(id= 3,nombre="Maria", apellidos="Lopez", password="1234", email="prueba3@gmail.com", tipo=2, img="https://www.google.com", fecha_nacimiento="1999-01-01", sexo="Mujer")
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


def crear_plataforma(request):
    img_dir = 'static/img'  # directory where images are stored
    for filename in os.listdir(img_dir):
        if filename.endswith(".svg"):  # check if the file is an image
            img_path = os.path.join(img_dir, filename)
            with open(img_path, 'rb') as img_file:
                crea = plataforma(nombre=os.path.splitext(filename)[0], img=File(img_file))
                crea.save()
    return HttpResponse(f"{crea}")

def crear_serie(request):
    serie1 = serie(nombre="The Witcher", sinopsis="Geralt de Rivia, un cazador de monstruos solitario, lucha por encontrar su lugar en un mundo donde las personas a menudo son más malvadas que las bestias.", img="https://pics.filmaffinity.com/the_witcher-737807462-mmed.jpg", trailer="https://www.youtube.com/watch?v=ndl1W4ltcmg", director="Lauren Schmidt Hissrich")
    serie1.save()
    serie2 = serie(nombre="The Mandalorian", sinopsis="The Mandalorian es una serie de televisión web de espacio occidental estadounidense que se estrenó en Disney+ el 12 de noviembre de 2019. Ambientada en el universo de Star Wars, la serie tiene lugar cinco años después de los eventos de El retorno del Jedi y sigue a un pistolero solitario más allá de los límites de la Nueva República.", img="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTE5IGVtPm4r5jG-dlf9tQ2Ymc8wu-CgsiaVu2M9VL4_3s0XJd8", trailer="https://www.youtube.com/watch?v=eW7Twd85m2g", director="Jon Favreau")
    serie2.save()
    serie3 = serie(nombre="Breaking Bad", sinopsis="Breaking Bad es una serie de televisión dramática estadounidense creada y producida por Vince Gilligan. La serie se estrenó el 20 de enero de 2008 en la cadena de televisión por cable AMC y finalizó el 29 de septiembre de 2013. Se conoce por su personaje principal, Walter White, un profesor de química de secundaria que se convierte en un narcotraficante después de ser diagnosticado con cáncer de pulmón.", img="https://m.media-amazon.com/images/M/MV5BYmQ4YWMxYjUtNjZmYi00MDQ1LWFjMjMtNjA5ZDdiYjdiODU5XkEyXkFqcGdeQXVyMTMzNDExODE5._V1_.jpg", trailer="https://www.youtube.com/watch?v=HhesaQXLuRY", director="Vince Gilligan")
    serie3.save()
    return HttpResponse(f"Serie creada")

def crear_foro_serie(request):
    foro1 = foro_serie(serie=serie.objects.get(id=1))
    foro1.save()
    foro2 = foro_serie(serie=serie.objects.get(id=2))
    foro2.save()
    foro3 = foro_serie(serie=serie.objects.get(id=3))
    foro3.save()
    return HttpResponse(f"Foro de serie creado")

def crear_foro_pelicula(request):
    foro1 = foro_pelicula(pelicula=pelicula.objects.get(id=1))
    foro1.save()
    foro2 = foro_pelicula(pelicula=pelicula.objects.get(id=2))
    foro2.save()
    foro3 = foro_pelicula(pelicula=pelicula.objects.get(id=3))
    foro3.save()
    return HttpResponse(f"Foro de pelicula creado")
def crear_comentario_serie(request):
    comentario1 = comentario_serie(contenido="Me encanta esta serie", visibilidad=True, usuario=Usuario.objects.get(id=1), foro_series=foro_serie.objects.get(id=1))
    comentario1.save()
    comentario2 = comentario_serie(contenido="Me encanta esta serie", visibilidad=True, usuario=Usuario.objects.get(id=2), foro_series=foro_serie.objects.get(id=2))
    comentario2.save()
    comentario3 = comentario_serie(contenido="Me encanta esta serie", visibilidad=True, usuario=Usuario.objects.get(id=3), foro_series=foro_serie.objects.get(id=3))
    comentario3.save()
    return HttpResponse(f"Comentario de serie creado")

def crear_comentario_pelicula(request):
    comentario1 = comentario_pelicula(contenido="Me encanta esta pelicula", visibilidad=True, usuario=Usuario.objects.get(id=1), foro_peliculas=foro_pelicula.objects.get(id=1))
    comentario1.save()
    comentario2 = comentario_pelicula(contenido="Me encanta esta pelicula", visibilidad=True, usuario=Usuario.objects.get(id=2), foro_peliculas=foro_pelicula.objects.get(id=2))
    comentario2.save()
    comentario3 = comentario_pelicula(contenido="Me encanta esta pelicula", visibilidad=True, usuario=Usuario.objects.get(id=3), foro_peliculas=foro_pelicula.objects.get(id=3))
    comentario3.save()
    return HttpResponse(f"Comentario de pelicula creado")

def crear_respuestas_series(request):
    respuesta1 = respuestas_series(contenido="Me encanta esta serie", visibilidad=True, usuario=Usuario.objects.get(id=1), comentario_series=comentario_serie.objects.get(id=1))
    respuesta1.save()
    respuesta2 = respuestas_series(contenido="Me encanta esta serie", visibilidad=True, usuario=Usuario.objects.get(id=2), comentario_series=comentario_serie.objects.get(id=2))
    respuesta2.save()
    respuesta3 = respuestas_series(contenido="Me encanta esta serie", visibilidad=True, usuario=Usuario.objects.get(id=3), comentario_series=comentario_serie.objects.get(id=3))
    respuesta3.save()
    return HttpResponse(f"Respuesta de serie creada")

def crear_respuestas_peliculas(request):
    respuesta1 = respuestas_peliculas(contenido="Me encanta esta pelicula", visibilidad=True, usuario=Usuario.objects.get(id=1), comentario_peliculas=comentario_pelicula.objects.get(id=1))
    respuesta1.save()
    respuesta2 = respuestas_peliculas(contenido="Me encanta esta pelicula", visibilidad=True, usuario=Usuario.objects.get(id=2), comentario_peliculas=comentario_pelicula.objects.get(id=2))
    respuesta2.save()
    respuesta3 = respuestas_peliculas(contenido="Me encanta esta pelicula", visibilidad=True, usuario=Usuario.objects.get(id=3), comentario_peliculas=comentario_pelicula.objects.get(id=3))
    respuesta3.save()
    return HttpResponse(f"Respuesta de pelicula creada")

def crear_temporada(request):
    temporada1 = temporada(nombre="Temporada 1", sinopsis="texto", img="https://www.google.com", fecha_estreno="2001-01-01", serie=serie.objects.get(id=1))
    temporada1.save()
    temporada2 = temporada(nombre="Temporada 2", sinopsis="texto", img="https://www.google.com", fecha_estreno="2002-01-01", serie=serie.objects.get(id=2))
    temporada2.save()
    temporada3 = temporada(nombre="Temporada 3", sinopsis="texto", img="https://www.google.com", fecha_estreno="2003-01-01", serie=serie.objects.get(id=3))
    temporada3.save()
    return HttpResponse(f"Temporada creada")

def crear_capitulo(request):
    capitulo1 = capitulo(nombre="Capitulo 1", sinopsis="texto", img="https://www.google.com", fecha_estreno="2003-01-01", temporada=temporada.objects.get(id=1))
    capitulo1.save()
    capitulo2 = capitulo(nombre="Capitulo 2", sinopsis="texto", img="https://www.google.com", fecha_estreno="2003-01-01", temporada=temporada.objects.get(id=2))
    capitulo2.save()
    capitulo3 = capitulo(nombre="Capitulo 3", sinopsis="texto", img="https://www.google.com", fecha_estreno="2003-01-01", temporada=temporada.objects.get(id=3))
    capitulo3.save()
    return HttpResponse(f"Capitulo creado")

def crear_valoracion_serie(request):
    valoracion1 = valoracion_serie(valoracion=5, estado=1, ultimo_capitulo=1, usuario=Usuario.objects.get(id=1), serie=serie.objects.get(id=1))
    valoracion1.save()
    valoracion2 = valoracion_serie(valoracion=5, estado=1, ultimo_capitulo=1, usuario=Usuario.objects.get(id=2), serie=serie.objects.get(id=2))
    valoracion2.save()
    valoracion3 = valoracion_serie(valoracion=5, estado=1, ultimo_capitulo=1, usuario=Usuario.objects.get(id=3), serie=serie.objects.get(id=3))
    valoracion3.save()
    return HttpResponse(f"Valoracion de serie creada")

def crear_valoracion_pelicula(request):
    valoracion1 = valoracion_pelicula(valoracion=5, estado=1, usuario=Usuario.objects.get(id=1), pelicula=pelicula.objects.get(id=1))
    valoracion1.save()
    valoracion2 = valoracion_pelicula(valoracion=5, estado=1, usuario=Usuario.objects.get(id=2), pelicula=pelicula.objects.get(id=2))
    valoracion2.save()
    valoracion3 = valoracion_pelicula(valoracion=5, estado=1, usuario=Usuario.objects.get(id=3), pelicula=pelicula.objects.get(id=3))
    valoracion3.save()
    return HttpResponse(f"Valoracion de pelicula creada")

def crear_pelicula_favorita(request):
    pelicula_favorita1 = peliculas_favoritas(usuario=Usuario.objects.get(id=1), pelicula=pelicula.objects.get(id=1))
    pelicula_favorita1.save()
    pelicula_favorita2 = peliculas_favoritas(usuario=Usuario.objects.get(id=2), pelicula=pelicula.objects.get(id=2))
    pelicula_favorita2.save()
    pelicula_favorita3 = peliculas_favoritas(usuario=Usuario.objects.get(id=3), pelicula=pelicula.objects.get(id=3))
    pelicula_favorita3.save()
    return HttpResponse(f"Pelicula favorita creada")

def crear_serie_favorita(request):
    serie_favorita1 = series_favoritas(usuario=Usuario.objects.get(id=1), serie=serie.objects.get(id=1))
    serie_favorita1.save()
    serie_favorita2 = series_favoritas(usuario=Usuario.objects.get(id=2), serie=serie.objects.get(id=2))
    serie_favorita2.save()
    serie_favorita3 = series_favoritas(usuario=Usuario.objects.get(id=3), serie=serie.objects.get(id=3))
    serie_favorita3.save()
    return HttpResponse(f"Serie favorita creada")

def crear_plataforma_pelicula(request):
    plataforma_pelicula1 = plataforma_pelicula(plataforma=plataforma.objects.get(id=1), pelicula=pelicula.objects.get(id=1))
    plataforma_pelicula1.save()
    plataforma_pelicula2 = plataforma_pelicula(plataforma=plataforma.objects.get(id=2), pelicula=pelicula.objects.get(id=2))
    plataforma_pelicula2.save()
    plataforma_pelicula3 = plataforma_pelicula(plataforma=plataforma.objects.get(id=3), pelicula=pelicula.objects.get(id=3))
    plataforma_pelicula3.save()
    return HttpResponse(f"Plataforma de pelicula creada")

def crear_plataforma_series(request):
    plataforma_serie1 = plataforma_serie(plataforma=plataforma.objects.get(id=1), serie=serie.objects.get(id=1))
    plataforma_serie1.save()
    plataforma_serie2 = plataforma_serie(plataforma=plataforma.objects.get(id=2), serie=serie.objects.get(id=2))
    plataforma_serie2.save()
    plataforma_serie3 = plataforma_serie(plataforma=plataforma.objects.get(id=3), serie=serie.objects.get(id=3))
    plataforma_serie3.save()
    return HttpResponse(f"Plataforma de serie creada")

def crear_personaje_pelicula(request):
    personaje_pelicula1 = personaje_pelicula(nombre_personaje="Harry Potter", actor=actor.objects.get(id=1), pelicula=pelicula.objects.get(id=1))
    personaje_pelicula1.save()
    personaje_pelicula2 = personaje_pelicula(nombre_personaje="Harry Potter", actor=actor.objects.get(id=2), pelicula=pelicula.objects.get(id=2))
    personaje_pelicula2.save()
    personaje_pelicula3 = personaje_pelicula(nombre_personaje="Harry Potter", actor=actor.objects.get(id=3), pelicula=pelicula.objects.get(id=3))
    personaje_pelicula3.save()
    return HttpResponse(f"Personaje de pelicula creado")
def crear_personaje_series(request):
    personaje_serie1 = personaje_serie(nombre_personaje="Geralt de Rivia", actor=actor.objects.get(id=1), serie=serie.objects.get(id=1))
    personaje_serie1.save()
    personaje_serie2 = personaje_serie(nombre_personaje="Geralt de Rivia", actor=actor.objects.get(id=2), serie=serie.objects.get(id=2))
    personaje_serie2.save()
    personaje_serie3 = personaje_serie(nombre_personaje="Geralt de Rivia", actor=actor.objects.get(id=3), serie=serie.objects.get(id=3))
    personaje_serie3.save()
    return HttpResponse(f"Personaje de serie creado")

def crear_pelicula_genero(request):
    pelicula_genero1 = pelicula_genero(genero=genero.objects.get(id=1), pelicula=pelicula.objects.get(id=1))
    pelicula_genero1.save()
    pelicula_genero2 = pelicula_genero(genero=genero.objects.get(id=2), pelicula=pelicula.objects.get(id=2))
    pelicula_genero2.save()
    pelicula_genero3 = pelicula_genero(genero=genero.objects.get(id=3), pelicula=pelicula.objects.get(id=3))
    pelicula_genero3.save()
    return HttpResponse(f"Genero de pelicula creado")

def crear_serie_genero(request):
    serie_genero1 = serie_genero(genero=genero.objects.get(id=1), serie=serie.objects.get(id=1))
    serie_genero1.save()
    serie_genero2 = serie_genero(genero=genero.objects.get(id=2), serie=serie.objects.get(id=2))
    serie_genero2.save()
    serie_genero3 = serie_genero(genero=genero.objects.get(id=3), serie=serie.objects.get(id=3))
    serie_genero3.save()
    return HttpResponse(f"Genero de serie creado")


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        return render(request, '')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        nombre_completo = request.POST.get('nombre_completo')
        mail = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmacion = request.POST.get('password_confirmacion')

        errors = []

        if password != password_confirmacion:
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
            user = Usuario.objects.create_user(username=username, email=mail, password=make_password(password), nombre_completo=nombre_completo)
            user.save()
            return redirect("login")


def reset_password(request):
    if request.method == 'GET':
        return render(request, 'reset_password.html')
    else:
        return render(request, 'reset_password.html')