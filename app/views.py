import random

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
from django.views.decorators.csrf import csrf_exempt

from .models import *

import json
from django.http import HttpResponse, JsonResponse


def mostrar_admi(request):
    return render(request, 'admi_pelicula.html')


def mostrar_peliculas(request):
    peliculas = pelicula.objects.all()
    return render(request, 'admi_pelicula.html', {'peliculas': peliculas})


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
    """add_peliculas_json()
    add_series_json()"""
    headerP = list(pelicula.objects.order_by('?')[:5])
    headerS = list(serie.objects.order_by('?')[:5])
    headerPS = headerP + headerS
    random.shuffle(headerPS)
    series = serie.objects.all().order_by('?')
    peliculas = pelicula.objects.all().order_by('?')
    return render(request, 'user_home.html', {'header': headerPS, 'series': series, 'peliculas': peliculas})


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
            user = User.objects.create(username=username, email=mail, password=make_password(password),
                                       nombre_completo=nombre_completo)
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
        return render(request, 'admi_pelicula.html', {'peliculas': uno})
    else:
        new = pelicula()
        new.nombre = request.POST.get('nombre')
        new.sinopsis = request.POST.get('sinopsis')
        new.anyo_estreno = request.POST.get('fecha_estreno')
        new.img = request.POST.get('img')
        new.trailer = request.POST.get('url_trailer')
        new.director = request.POST.get('director')
        new.save()

        return redirect('/administrador/pelicula')


def new_serie(request):
    if request.method == 'GET':
        uno = serie.objects.all()
        return render(request, 'admi_series.html', {'serie': uno})
    else:
        new = serie()
        new.nombre = request.POST.get('nombre_serie')
        new.sinopsis = request.POST.get('sinopsis_serie')
        new.anyo_estreno = request.POST.get('fecha_estreno_serie')
        new.img = request.POST.get('img_serie')
        new.trailer = request.POST.get('trailer_serie')
        new.director = request.POST.get('director_serie')
        new.save()

        return redirect('/administrador/series_actuales')

def new_actor(request):
    if request.method == 'GET':
        uno = actor.objects.all()
        return render(request, 'admi_actores.html', {'actor': uno})
    else:
        new = actor()
        new.nombre = request.POST.get('nombre_actor')
        new.img = request.POST.get('img_actor')
        new.save()

        return redirect('/administrador/listado_actores')

def mostrar_series(request):
    ser = serie.objects.all()
    return render(request, 'admi_series.html', {'series': ser})


def mostrar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'admi_usuarios.html', {'usuarios': usuarios})

def mostrar_actores(request):
    actores = actor.objects.all()
    return render(request, 'admi_actores.html', {'actores': actores})

def eliminar_actor(request, id):
    actor_eliminar = actor.objects.get(id=id)
    actor_eliminar.delete()
    return redirect('/administrador/listado_actores')

def eliminar_usuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect('/administrador/usuarios')


def eliminar_pelicula(request, id):
    pelicula_eliminar = pelicula.objects.get(id=id)
    pelicula_eliminar.delete()
    return redirect('/administrador/pelicula')


def eliminar_serie(request, id):
    serie_eliminar = serie.objects.get(id=id)
    serie_eliminar.delete()
    return redirect('/administrador/series_actuales')


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

        return redirect('/administrador/pelicula')


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

        return redirect('/administrador/series_actuales')

def editar_actor(request, id):
    actor_editar = actor.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'editar_actor.html', {'actor': actor_editar})
    else:
        actor_editar.nombre = request.POST.get('nombre')
        actor_editar.img = request.POST.get('img')
        actor_editar.save()

        return redirect('/administrador/listado_actores')



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
    # add_plataformas()
    user = User.objects.get(id=request.user.id)
    user_plataformas = user.usuario_plataforma_set.all()
    plataformas_totales = plataforma.objects.all()
    plataformas_1 = [up.plataforma for up in user_plataformas]
    if user is not None:
        return render(request, 'plataformas.html',
                      {'user': user, 'plataformas': plataformas_1, 'totales': plataformas_totales})
    else:
        return render(request, 'login.html')


def add_plataformas():
    # Directory where the images are located
    directory = os.path.join(settings.MEDIA_ROOT, 'plataformas')  # Iterate over all files in the directory
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
def load_movies_data(request):
    add_peliculas_json()
    return HttpResponse("Datos de películas cargados correctamente")


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
def load_series_data(request):
    add_series_json()
    return HttpResponse("Datos de series cargados correctamente")


def view_peliculas(request):
    peliculas = pelicula.objects.all()
    return render(request, 'peliculas.html', {'peliculas': peliculas})


def view_series(request):
    series = serie.objects.all()
    return render(request, 'series.html', {'series': series})


def mostrar_pelicula(request, id_pelicula):
    peli = pelicula.objects.get(id=id_pelicula)
    plt_pelicula = plataforma_pelicula.objects.filter(pelicula_id=peli).all()
    gen_pelicula = pelicula_genero.objects.filter(pelicula_id=peli).all()
    pj_pelicula = personaje_pelicula.objects.filter(pelicula_id=peli).all()[:6]
    return render(request, 'vista_pelicula.html', {'pelicula': peli, 'plt': plt_pelicula, 'gen': gen_pelicula, 'pj': pj_pelicula})


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
    return redirect('plataformas')


def configurar_perfil(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        if 'foto_perfil' in request.FILES:  # Verificar si 'foto_perfil' está en request.FILES
            foto_perfil = request.FILES['foto_perfil']
            user.img = foto_perfil
        user.fecha_nacimiento = request.POST.get('user_fecha_nacimiento')
        user.sexo = request.POST.get('user_sexo')
        user.username = request.POST.get('user_username')
        user.nombre_completo = request.POST.get('user_nombre_completo')
        user.save()
        return redirect('configuracion')
    return redirect('configuracion')

def mostrar_generos(request):
    generos = genero.objects.all()
    return render(request, 'admi_genero.html', {'generos': generos})

def add_uniones_peliculas(request, id):
    pelicula_instancia = pelicula.objects.get(id=id)
    pelicula_generos = pelicula_instancia.pelicula_genero_set.all()
    generos_totales = genero.objects.all()
    generos_vinculados = [up.genero for up in pelicula_generos]
    plataformas_totales = plataforma.objects.all()
    pelicula_plataforma = pelicula_instancia.plataforma_pelicula_set.all()
    plataformas_vinculadas = [up.plataforma for up in pelicula_plataforma]
    if request.method == 'GET':
        return render(request, 'unir_pelicula.html', {'pelicula': pelicula_instancia, 'generos': generos_totales ,'genero_vinculado': generos_vinculados, 'plataformas_totales': plataformas_totales, 'plataformas_vinculadas': plataformas_vinculadas,'actores': actor.objects.all()})
    else:

        return redirect('/administrador/listado_actores')

def new_genero(request):
    if request.method == 'GET':
        uno = genero.objects.all()
        return render(request, 'admi_genero.html', {'generos': uno})
    else:
        new = genero()
        new.nombre = request.POST.get('nombre')
        new.descripcion = request.POST.get('descripcion')
        new.save()

        return redirect('/administrador/listado_generos')

def add_vinculacion_genero_json():
    with open('static/Generos.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Itera sobre cada elemento en los datos
    for gen in data:
        g = genero()
        g.nombre = gen['nombre']
        g.descripcion = gen['descripcion']
        g.save()
def editar_genero(request, id):
    genero_editar = genero.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'editar_genero.html', {'genero': genero_editar})
    else:
        genero_editar.nombre = request.POST.get('nombre')
        genero_editar.descripcion = request.POST.get('descripcion')
        genero_editar.save()

        return redirect('/administrador/listado_generos')
def vincular_desvincular_genero_pelicula(request, id):
    genero_id = request.GET.get('generoId')
    # Obtén las instancias completas de la película y el género
    pelicula_instancia = pelicula.objects.get(id=id)
    genero_instancia = genero.objects.get(id=genero_id)
    try:
        # Intenta obtener la relación existente entre la película y el género
        gen_pel = pelicula_genero.objects.get(pelicula=pelicula_instancia, genero=genero_instancia)
    except pelicula_genero.DoesNotExist:
        # Si la relación no existe, se crea
        pelicula_genero.objects.create(pelicula=pelicula_instancia, genero=genero_instancia)
    else:
        # Si la relación existe, se elimina
        gen_pel.delete()
    return redirect('vincular_pelicula', id=pelicula_instancia.id)

def vincular_desvincular_plataforma_pelicula(request, id):
    plataformaId = request.GET.get('plataformaId')
    plataforma_instancia = plataforma.objects.get(id=plataformaId)
    try:
        pla_pel = plataforma_pelicula.objects.get(plataforma=plataforma_instancia, pelicula=pelicula.objects.get(id=id))
    except plataforma_pelicula.DoesNotExist:
        # Si la relación no existe, se crea
        plataforma_pelicula.objects.create(plataforma=plataforma_instancia, pelicula=pelicula.objects.get(id=id))
    else:
        # Si la relación existe, se elimina
        pla_pel.delete()
    return redirect('vincular_pelicula', id=id)

def vinculacion_genero_pelicula_json():
    with open('static/Generos_Peliculas.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Itera sobre cada elemento en los datos
        for gen in data:
            g = pelicula_genero()
            g.pelicula_id = gen['id_pelicula']
            g.genero_id = gen['id_genero']
            g.save()
def vinculacion_genero_serie_json():
    with open('static/Generos_Series.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Itera sobre cada elemento en los datos
        for gen in data:
            g = serie_genero()
            g.serie_id = gen['id_serie']
            g.genero_id = gen['id_genero']
            g.save()

def cargar_datos_sql(request):
    add_series_json()
    add_peliculas_json()
    add_plataformas()
    add_vinculacion_genero_json()
    vinculacion_genero_pelicula_json()
    vinculacion_genero_serie_json()
    return HttpResponse("Datos de generos cargados correctamente")