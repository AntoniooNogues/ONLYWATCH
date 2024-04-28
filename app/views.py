from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

import os
from django.contrib import messages
from django.core.files import File
import random
import smtplib
from django.core.mail import send_mail
# Create your views here
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.conf import settings
# Create your views here.
from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse


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
    headerPyS = pelicula.objects.all()[:5].random + serie.objects.all()[:5].random
    p = pelicula.objects.all()
    return render(request, 'user_home.html', {'header': headerPyS, 'pelicula': p})

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
    user = User.objects.get(id=request.user.id)
    user_plataformas = user.usuario_plataforma_set.all()
    plataformas_totales = plataforma.objects.all()
    plataformas_1 = [up.plataforma for up in user_plataformas]
    if user is not None:
        return render(request, 'User_information.html', {'user': user, 'plataformas': plataformas_1, 'totales': plataformas_totales})
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

# def calcular_edad(fecha_nacimiento):
#     nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
#     hoy = datetime.now()
#     edad = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))
#     return edad
# edad = calcular_edad(User.fecha_nacimiento)

# def generate_code():
#     return random.randint(100000, 999999)
#
# def send_email(user_email, code):
#     send_mail(
#         'Codigo de verificación',
#         f'Tu codigo de verificación es {code}',
#         'onlywatch.info@gmail.es',
#         [user_email],
#         fail_silently=False,
#     )
#
# def verify_code(user_input, code):
#     return user_input == code



def send_verification_code(request):
    if request.method == 'POST':
        code = random.randint(100000, 999999)
        send_mail(
            'Código de verificación',
            f'Tu código de verificación es {code}',
            'onlywatch.info@gmail.es',
            [request.user.email],
            fail_silently=False,
        )
        request.session['verification_code'] = code
        messages.success(request, 'Código de verificación enviado')
    return redirect(reverse('configuracion'))

def verify_code(request):
    if request.method == 'POST':
        user_code = int(request.POST['code'])
        verification_code = request.session.get('verification_code')
        if user_code == verification_code:
            del request.session['verification_code']
            return render(request,'reset_password.html')
        else:
            messages.error(request, 'Código de verificación incorrecto')
            return render(request, 'User_information.html')
    return redirect('configuracion')



def vincular_desvincular_plataforma(request, plataforma_id):
    try:
        user_plat = usuario_plataforma.objects.get(usuario=request.user, plataforma_id=plataforma_id)
    except usuario_plataforma.DoesNotExist:
        # Si la relación no existe, se crea
        usuario_plataforma.objects.create(usuario=request.user, plataforma_id=plataforma_id)
    else:
        # Si la relación existe, se elimina
        user_plat.delete()

    return redirect('configuracion')

def configurar_perfil(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        user.img = request.POST.get('foto_perfil')
        user.fecha_nacimiento = request.POST.get('user_fecha_nacimiento')
        user.sexo = request.POST.get('user_sexo')
        user.username = request.POST.get('user_username')
        user.nombre_completo = request.POST.get('user_nombre_completo')
        # Acceder al archivo de imagen enviado por el usuario
        if 'foto_perfil' in request.FILES:
            imagen = request.FILES['foto_perfil']
            user.img = imagen  # Guardar la imagen en el campo correspondiente del modelo de usuario

        user.save()
        return redirect('configuracion')
    return redirect('configuracion')


