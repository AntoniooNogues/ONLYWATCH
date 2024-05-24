import random
from django.db.models import QuerySet
from django.contrib import messages
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.core.mail import EmailMessage
from django.core.paginator import Paginator
from django.db.models import Avg
from django.db.models import Q
from django.db.models.fields import json
from django.http import HttpResponse, JsonResponse
# Create your views here
from django.shortcuts import get_object_or_404
# Create your views here.
from django.shortcuts import render
from django.template.loader import render_to_string
import re
import os
from .decorators import *
from .models import *

import json
from django.http import HttpResponse, JsonResponse

@check_user_role('ADMIN')
def mostrar_admi(request):
    return render(request, 'admi_pelicula.html')

@check_user_role('ADMIN')
def mostrar_peliculas(request):
    peliculas = pelicula.objects.all()
    return render(request, 'admi_pelicula.html', {'peliculas': peliculas})


def do_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        errors = []
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            errors.append("No se ha podido iniciar sesión intentalo de nuevo")
            return render(request, 'login.html', {"errores": errors})

    # Mostrar formulario de login para método GET
    return render(request, 'login.html')


def do_logout(request):
    logout(request)
    return redirect('login')

def slider_header():
    headerP = list(pelicula.objects.order_by('?')[:5])
    headerS = list(serie.objects.order_by('?')[:5])
    headerPS = headerP + headerS
    random.shuffle(headerPS)
    return headerPS

def paginacion(request, lista_series, lista_peliculas):
    if isinstance(lista_series, QuerySet) and isinstance(lista_peliculas, QuerySet):
        combined_list = list(lista_series) + list(lista_peliculas)
    elif isinstance(lista_series, list) and isinstance(lista_peliculas, list):
        combined_list = lista_series + lista_peliculas
    else:
        raise ValueError('Las listas deben ser del mismo tipo')
    # Paginacion de Home
    paginator = Paginator(combined_list, 20)  # Show 20 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj

def mostrar_inicio(request):
    series_list = list(serie.objects.all())
    peliculas_list = list(pelicula.objects.all())
    #Parte Superior de Home
    headerPS = slider_header()
    gen=genero.objects.all()
    plt = plataforma.objects.all()
    page_obj = paginacion(request, series_list, peliculas_list)

    return render(request, 'user_home.html', {'header': headerPS, 'page_obj': page_obj, 'generos': gen, 'plataformas': plt})

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('username')
        nombre_completo = request.POST.get('nombre_completo')
        mail = request.POST.get('email')
        password = request.POST.get('password1')
        password_confirmacion = request.POST.get('password2')

        errors = 0

        if password != password_confirmacion or len(password) < 8 or not re.search(r"\d", password) or not re.search(
                r"[A-Z]", password):
            errors += 1
            messages.add_message(request, messages.WARNING, "Contraseña no válida")

        existe_usuario = User.objects.filter(username=username).exists()
        if existe_usuario:
            errors += 1
            messages.add_message(request, messages.WARNING, "Ya existe un usuario con ese nombre")
        existe_mail = User.objects.filter(email=mail).exists()
        if existe_mail:
            errors += 1
            messages.add_message(request, messages.WARNING, "Ya existe un usuario con ese email")


        if errors != 0:
            return render(request, 'register.html', {'messages': messages.get_messages(request)})
        else:
            user = User.objects.create(username=username, email=mail, password=make_password(password), nombre_completo=nombre_completo)
            user.save()
            return redirect('login')


def reset_password(request):
    if request.method == 'GET':
        return render(request, 'reset_password.html')
    else:
        return render(request, 'reset_password.html')

@check_user_role('ADMIN')
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

        return redirect('/administracion/pelicula')

@check_user_role('ADMIN')
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

        return redirect('/administracion/series_actuales')

@check_user_role('ADMIN')
def new_actor(request):
    if request.method == 'GET':
        uno = actor.objects.all()
        return render(request, 'admi_actores.html', {'actor': uno})
    else:
        new = actor()
        new.nombre = request.POST.get('nombre_actor')
        new.save()

        return redirect('/administracion/listado_actores')


@check_user_role('ADMIN')
def mostrar_series(request):
    ser = serie.objects.all()
    return render(request, 'admi_series.html', {'series': ser})


@check_user_role('ADMIN')
def mostrar_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'admi_usuarios.html', {'usuarios': usuarios})


@check_user_role('ADMIN')
def mostrar_actores(request):
    actores = actor.objects.all()
    return render(request, 'admi_actores.html', {'actores': actores})


@check_user_role('ADMIN')
def eliminar_actor(request, id):
    actor_eliminar = actor.objects.get(id=id)
    actor_eliminar.delete()
    return redirect('/administracion/listado_actores')


@check_user_role('ADMIN')
def eliminar_usuario(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect('/administracion/usuarios')


@check_user_role('ADMIN')
def eliminar_pelicula(request, id):
    pelicula_eliminar = pelicula.objects.get(id=id)
    pelicula_eliminar.delete()
    return redirect('/administracion/pelicula')


@check_user_role('ADMIN')
def eliminar_serie(request, id):
    serie_eliminar = serie.objects.get(id=id)
    serie_eliminar.delete()
    return redirect('/administracion/series_actuales')



@check_user_role('ADMIN')
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

        return redirect('/administracion/pelicula')


@check_user_role('ADMIN')
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

        return redirect('/administracion/series_actuales')


@check_user_role('ADMIN')
def editar_actor(request, id):
    actor_editar = actor.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'editar_actor.html', {'actor': actor_editar})
    else:
        actor_editar.nombre = request.POST.get('nombre')
        actor_editar.img = request.POST.get('img')
        actor_editar.save()

        return redirect('/administracion/listado_actores')



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



def view_peliculas(request):
    peliculas = pelicula.objects.all()
    gen = genero.objects.all()
    plt = plataforma.objects.all()
    if request.user.is_authenticated:
        for p in peliculas:
            valoracion_media = valoracion_pelicula.objects.filter(pelicula=p).aggregate(Avg('valoracion'))['valoracion__avg']
            p.valoracion_media = valoracion_media
            es_favorito = peliculas_favoritas.objects.filter(usuario=request.user, pelicula=p).exists()
            p.es_favorito = es_favorito
        paginator = Paginator(peliculas, 20)  # Show 20 items per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'peliculas.html', {'peliculas': peliculas, 'page_obj': page_obj, 'generos': gen, 'plataformas': plt})
    else:
        paginator = Paginator(peliculas, 20)  # Show 20 items per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'peliculas.html', {'peliculas': peliculas, 'page_obj': page_obj, 'generos': gen, 'plataformas': plt})



def view_series(request):
    series = serie.objects.all()
    gen = genero.objects.all()
    plt = plataforma.objects.all()
    if request.user.is_authenticated:
        for s in series:
            valoracion_media = valoracion_serie.objects.filter(serie=s).aggregate(Avg('valoracion'))[
                'valoracion__avg']
            s.valoracion_media = 'No valorado' if valoracion_media is None else valoracion_media
            s.es_favorito = series_favoritas.objects.filter(usuario=request.user, serie=s).exists()
        paginator = Paginator(series, 20)  # Show 20 items per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'series.html', {'series': series, 'page_obj': page_obj, 'generos': gen, 'plataformas': plt})
    else:
        paginator = Paginator(series, 20)  # Show 20 items per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'series.html', {'series': series, 'page_obj': page_obj, 'generos': gen, 'plataformas': plt})


def mostrar_pelicula(request, id_pelicula):
    if request.user.is_authenticated:
        peli = pelicula.objects.get(id=id_pelicula)
        plt_pelicula = plataforma_pelicula.objects.filter(pelicula_id=peli).all()
        gen_pelicula = pelicula_genero.objects.filter(pelicula_id=peli).all()
        pj_pelicula = personaje_pelicula.objects.filter(pelicula_id=peli).all()[:6]
        es_favorito = peliculas_favoritas.objects.filter(usuario=request.user, pelicula=peli).exists()
        valoracion_media = valoracion_pelicula.objects.filter(pelicula=peli).aggregate(Avg('valoracion'))
        foro = foro_pelicula.objects.get(pelicula_id=id_pelicula)
        comentarios = comentario_pelicula.objects.filter(foro_peliculas_id=foro.id).all()
        for c in comentarios:
            c.user = User.objects.get(id=c.usuario_id)
            try:
                valoracion = valoracion_pelicula.objects.get(usuario=User.objects.get(id=c.usuario_id), pelicula=peli).valoracion
            except valoracion_pelicula.DoesNotExist:
                valoracion = None

            # Asignar 'No tiene valoracion' si la valoración es None
            c.valoracion_usuario = valoracion if valoracion is not None else ''

        return render(request, 'vista_pelicula.html',
                      {'pelicula': peli, 'plt': plt_pelicula, 'gen': gen_pelicula, 'pj': pj_pelicula, 'es_favorito': es_favorito, 'valoracion_media': valoracion_media, 'comentarios': comentarios})
    else:
        peli = pelicula.objects.get(id=id_pelicula)
        plt_pelicula = plataforma_pelicula.objects.filter(pelicula_id=peli).all()
        gen_pelicula = pelicula_genero.objects.filter(pelicula_id=peli).all()
        pj_pelicula = personaje_pelicula.objects.filter(pelicula_id=peli).all()[:6]
        valoracion_media = valoracion_pelicula.objects.filter(pelicula=peli).aggregate(Avg('valoracion'))
        return render(request, 'vista_pelicula.html', {'pelicula': peli, 'plt': plt_pelicula, 'gen': gen_pelicula, 'pj': pj_pelicula, 'valoracion_media': valoracion_media})

    return render(request, 'vista_pelicula.html', {'pelicula': peli, 'plt': plt_pelicula, 'gen': gen_pelicula, 'pj': pj_pelicula, 'es_favorito': es_favorito, 'valoracion_media': valoracion_media})

def mostrar_serie(request, id_serie):
    if request.user.is_authenticated:
        serie_editar = serie.objects.get(id=id_serie)
        temporadas = temporada.objects.filter(serie_id=serie_editar).distinct()
        capitulos = capitulo.objects.filter(temporada__serie_id=serie_editar)
        plt_serie = plataforma_serie.objects.filter(serie_id=serie_editar).all()
        gen_serie = serie_genero.objects.filter(serie_id=serie_editar).all()
        pj_serie = personaje_serie.objects.filter(serie_id=serie_editar).all()[:6]
        es_favorito = series_favoritas.objects.filter(usuario=request.user, serie=serie_editar).exists()
        valoracion_media = valoracion_serie.objects.filter(serie=serie_editar).aggregate(Avg('valoracion'))
        foro = foro_serie.objects.get(serie_id=id_serie)
        comentarios = comentario_serie.objects.filter(foro_series_id=foro.id).all()
        for c in comentarios:
            c.user = User.objects.get(id=c.usuario_id)
            try:
                valoracion = valoracion_serie.objects.get(usuario=User.objects.get(id=c.usuario_id), serie=serie_editar).valoracion
            except valoracion_serie.DoesNotExist:
                valoracion = None

            # Asignar 'No tiene valoracion' si la valoración es None
            c.valoracion_usuario = valoracion if valoracion is not None else ''
        return render(request, 'vista_serie.html',
                      {'serie': serie_editar, 'plt': plt_serie, 'gen': gen_serie, 'pj': pj_serie,
                       'es_favorito': es_favorito, 'valoracion_media': valoracion_media, 'comentarios': comentarios, "temporadas": temporadas,
                       "capitulos": capitulos})
    else:
        serie_editar = serie.objects.get(id=id_serie)
        temporadas = temporada.objects.filter(serie_id=id_serie)
        capitulos = capitulo.objects.filter(temporada__serie_id=id_serie)
        plt_serie = plataforma_serie.objects.filter(serie_id=serie_editar).all()
        gen_serie = serie_genero.objects.filter(serie_id=serie_editar).all()
        pj_serie = personaje_serie.objects.filter(serie_id=serie_editar).all()[:6]
        valoracion_media = valoracion_serie.objects.filter(serie=serie_editar).aggregate(Avg('valoracion'))
        return render(request, 'vista_serie.html',
                      {'serie': serie_editar, 'plt': plt_serie, 'gen': gen_serie, 'pj': pj_serie,
                       'valoracion_media': valoracion_media, "temporadas": temporadas,
                       "capitulos": capitulos})


def send_verification_code(request):
    if request.method == 'POST':
        code = random.randint(100000, 999999)
        context = {
            'code': code,
        }
        email_html_message = render_to_string('modelo_email.html', context)
        email = EmailMessage(
            'Codigo de verificación',
            email_html_message,
            'onlywatch.info@gmail.es',
            [request.user.email],
        )
        email.content_subtype = 'html'
        email.send()
        request.session['verification_code'] = code
        mensaje = "El mesaje ha sido enviado correctamente"
        return JsonResponse({'mensage': mensaje})
    else:
        mensaje = False
        return JsonResponse({'mensage': mensaje})

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


@check_user_role('ADMIN')
def add_uniones_peliculas(request, id):
    pelicula_instancia = pelicula.objects.get(id=id)
    pelicula_generos = pelicula_instancia.pelicula_genero_set.all()
    generos_totales = genero.objects.all()
    generos_vinculados = [up.genero for up in pelicula_generos]
    plataformas_totales = plataforma.objects.all()
    pelicula_plataforma = pelicula_instancia.plataforma_pelicula_set.all()
    plataformas_vinculadas = [up.plataforma for up in pelicula_plataforma]
    actores = actor.objects.all()
    personajes = personaje_pelicula.objects.filter(pelicula_id=id)

    if request.method == 'GET':
        return render(request, 'unir_pelicula.html', {'pelicula': pelicula_instancia, 'generos': generos_totales ,'genero_vinculado': generos_vinculados, 'plataformas_totales': plataformas_totales, 'plataformas_vinculadas': plataformas_vinculadas,'actores': actor.objects.all(), 'personajes': personajes})
    else:
        return redirect('vincular_pelicula', id=id)



@check_user_role('ADMIN')
def new_genero(request):
    if request.method == 'GET':
        uno = genero.objects.all()
        return render(request, 'admi_genero.html', {'generos': uno})
    else:
        new = genero()
        new.nombre = request.POST.get('nombre')
        new.descripcion = request.POST.get('descripcion')
        new.save()

        return redirect('/administracion/listado_generos')


def add_vinculacion_genero_json():
    with open('static/Generos.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Itera sobre cada elemento en los datos
    for gen in data:
        g = genero()
        g.nombre = gen['nombre']
        g.descripcion = gen['descripcion']
        g.save()


@check_user_role('ADMIN')
def editar_genero(request, id):
    genero_editar = genero.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'editar_genero.html', {'genero': genero_editar})
    else:
        genero_editar.nombre = request.POST.get('nombre')
        genero_editar.descripcion = request.POST.get('descripcion')
        genero_editar.save()

        return redirect('/administracion/listado_generos')



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

def vinculacion_plataforma_pelis_json():
    with open('static/Plataformas_Peliculas.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Itera sobre cada elemento en los datos
        for gen in data:
            g = plataforma_pelicula()
            g.pelicula_id = gen['pelicula_id']
            g.plataforma_id = gen['plataforma_id']
            g.save()
def vinculacion_plataforma_series_json():
    with open('static/Plataformas_Series.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Itera sobre cada elemento en los datos
        for gen in data:
            g = plataforma_serie()
            g.serie_id = gen['serie_id']
            g.plataforma_id = gen['plataforma_id']
            g.save()

def add_temporadas_json():
    with open('static/Temporadas.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Itera sobre cada elemento en los datos
        for d in data:
            tem = temporada()
            tem.nombre = d['nombre']
            tem.sinopsis = d['sinopsis']
            tem.img = d['img']
            tem.fecha_estreno = d['fecha_estreno']
            tem.serie_id = d['serie_id']
            tem.save()
        return HttpResponse("Datos de temporadas cargados correctamente")

def valorar_pelicula(request, id_pelicula):
    if request.method == 'POST':
        if request.user.is_authenticated:
            pelicula_valorar = get_object_or_404(pelicula, id=id_pelicula)
            valoracion = request.POST.get('valoracion')
            if int(valoracion) > 10 or int(valoracion) < 0:
                messages.error(request, 'La valoración solo es posible entre 0-10.')
                return redirect('pelicula', id_pelicula=id_pelicula)
            try:
               valor = valoracion_pelicula.objects.get(usuario=request.user, pelicula=pelicula_valorar)
               valor.valoracion = valoracion  # Update the existing rating
               valor.save()  # Save the updated rating
               messages.success(request, 'Tu valoración ha sido actualizada.')
            except valoracion_pelicula.DoesNotExist:
                valoracion_pelicula.objects.create(usuario=request.user, pelicula=pelicula_valorar, valoracion=valoracion)
                messages.success(request, 'Tu valoración ha sido registrada.')
            return redirect('pelicula', id_pelicula=id_pelicula)
        else:
            return redirect('pelicula', id_pelicula=id_pelicula)

def pelicula_favorita(request, id_pelicula):
    pelicula_instancia = get_object_or_404(pelicula, id=id_pelicula)
    try:
        fav = peliculas_favoritas.objects.get(usuario=request.user, pelicula=pelicula_instancia)
    except peliculas_favoritas.DoesNotExist:
        peliculas_favoritas.objects.create(usuario=request.user, pelicula=pelicula_instancia)
        es_favorito = True
        messages.success(request, '¡Te ha gustado esta película!')
    else:
        fav.delete()
        es_favorito = False
        messages.add_message(request, messages.WARNING, '¡Has quitado de favorito esta película!')
    messages_html = render_to_string('mensages.html', {'messages': messages.get_messages(request)})
    return JsonResponse({'es_favorito': es_favorito, 'messages_html': messages_html})



def valorar_serie(request):
    if request.method == 'POST':
        id_serie = request.POST.get('serie_id')
        if request.user.is_authenticated:
            serie_valorar = get_object_or_404(serie, id=id_serie)
            valoracion = request.POST.get('valoracion')
            if int(valoracion) > 10 or int(valoracion) < 0:
                messages.error(request, 'La valoración solo es posible entre 0-10.')
                return redirect('serie', id_serie=id_serie)
            try:
               valor = valoracion_serie.objects.get(usuario=request.user, serie=serie_valorar)
               valor.valoracion = valoracion  # Update the existing rating
               valor.save()  # Save the updated rating
               messages.success(request, 'Tu valoración ha sido actualizada.')
            except valoracion_serie.DoesNotExist:
                valoracion_serie.objects.create(usuario=request.user, serie=serie_valorar, valoracion=valoracion)
                messages.success(request, 'Tu valoración ha sido registrada.')
            return mostrar_serie(request, id_serie)
        else:
            return mostrar_serie(request, id_serie)

def serie_favorita(request, id_serie):
    serie_instancia = get_object_or_404(serie, id=id_serie)
    try:
        fav = series_favoritas.objects.get(usuario=request.user, serie=serie_instancia)
    except series_favoritas.DoesNotExist:
        series_favoritas.objects.create(usuario=request.user, serie=serie_instancia)
        es_favorito = True
        messages.success(request, '¡Te ha gustado esta serie!')
    else:
        fav.delete()
        es_favorito = False
        messages.add_message(request, messages.WARNING, '¡Has quitado de favorito esta serie!')
    messages_html = render_to_string('mensages.html', {'messages': messages.get_messages(request)})
    return JsonResponse({'es_favorito': es_favorito, 'messages_html': messages_html})

def login_admi(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            # Redirección tras un login exitoso
            return redirect('administracion_home')
        else:
            # Mensaje de error si la autenticación falla
            return render(request, 'login_admi.html', {"error": "No se ha podido iniciar sesión intentalo de nuevo"})

    # Mostrar formulario de login para método GET
    return render(request, 'login_admi.html')

def anadir_actores_personaje_serie(request):
    # Diccionario para almacenar actores únicos
    actores_unicos = {}
    actor_id = 303

    # Lista para personajes
    personajes = []

    # Leer el archivo pelicula_acotores_v1.json
    with open('static/serie_actores_v1.json', 'r', encoding='utf-8') as file:
        datos_peliculas = json.load(file)

    # Load the JSON file
    with open('static/actores.json', 'r', encoding='utf-8') as f:
        existing_actors = json.load(f)

    # Convert the list of dictionaries to a list of actor names
    existing_actor_names = [actor['nombre'] for actor in existing_actors]

    # Procesar datos
    for serie in datos_peliculas:
        serie_id = serie["serie_id"]
        for actor in serie["actores"]:
            nombre_actor = actor["nombre"]
            if nombre_actor not in existing_actor_names:
                actores_unicos[nombre_actor] = {
                    "id": actor_id,
                    "nombre": nombre_actor
                }
                actor_id += 1
            if nombre_actor in actores_unicos:
                personajes.append({
                    "nombre_personaje": actor["nombre_personaje"],
                    "actor_id": actores_unicos[nombre_actor]["id"],
                    "serie_id": serie_id
                })

    # Crear JSON para actores
    json_actores = [{"id": actor["id"], "nombre": actor["nombre"]} for actor in
                    actores_unicos.values()]

    # Crear JSON para personajes
    json_personajes = personajes

    existing_actors.extend(json_actores)

    # Guardar JSON en archivos
    with open('actores.json', 'w', encoding='utf-8') as f:
        json.dump(existing_actors, f, indent=4, ensure_ascii=False)

    with open('personaje_serie.json', 'w', encoding='utf-8') as f:
        json.dump(json_personajes, f, indent=4, ensure_ascii=False)

    return HttpResponse("JSON de actores y personajes generados con éxito.")

def anadir_actores():
    with open('static/actores.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Itera sobre cada elemento en los datos
    for gen in data:
        g = actor()
        g.id = gen['id']
        g.nombre = gen['nombre']
        g.save()
    return HttpResponse("Datos de actores cargados correctamente")

def anadir_personaje_pelicula():
    with open('static/personajes_pelicula.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Itera sobre cada elemento en los datos
    for gen in data:
        g = personaje_pelicula()
        g.nombre_personaje = gen['nombre_personaje']
        g.actor_id = gen['actor_id']
        g.pelicula_id = gen['pelicula_id']
        g.save()
    return HttpResponse("Datos de personajes de peliculas cargados correctamente")

def anadir_personaje_serie():
    with open('static/personaje_serie.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Itera sobre cada elemento en los datos
    for gen in data:
        g = personaje_serie()
        g.nombre_personaje = gen['nombre_personaje']
        g.actor_id = gen['actor_id']
        g.serie_id = gen['serie_id']
        g.save()
    return HttpResponse("Datos de personajes de series cargados correctamente")

def cargar_actores_personajes(request):
    anadir_actores()
    anadir_personaje_pelicula()
    anadir_personaje_serie()
    return HttpResponse("Datos de actores y personajes cargados correctamente")

def filtrar(request):
    headerPS = slider_header()
    generos = request.GET.getlist('generos')
    plataformas = request.GET.getlist('plataformas')

    if "Disney " in plataformas:
        plataformas.clear()
        plataformas.append("Disney+")

    if "Moviestar " in plataformas:
        plataformas.clear()
        plataformas.append("Moviestar+")

    if len(generos) == 0:
        fil_plt = plataforma.objects.filter(nombre__in=plataformas).values_list('id', flat=True)
        peliculas = pelicula.objects.filter(plataforma_pelicula__plataforma_id__in=fil_plt)
        series = serie.objects.filter(plataforma_serie__plataforma_id__in=fil_plt)

        gen = genero.objects.all()
        plt = plataforma.objects.all()
        return render(request, 'home_filtros.html', {'header': headerPS,  'generos': gen, 'plataformas': plt, 'peliculas': peliculas, 'series': series})
    elif len(plataformas) == 0:
        fil_gen = genero.objects.filter(nombre__in=generos).values_list('id', flat=True)
        peliculas = pelicula.objects.filter(pelicula_genero__genero_id__in=fil_gen)
        series = serie.objects.filter(serie_genero__genero_id__in=fil_gen)
        gen = genero.objects.all()
        plt = plataforma.objects.all()
        return render(request, 'home_filtros.html', {'header': headerPS,  'generos': gen, 'plataformas': plt, 'peliculas': peliculas, 'series': series})
    else:
        fil_gen = genero.objects.filter(nombre__in=generos).values_list('id', flat=True)
        fil_plt = plataforma.objects.filter(nombre__in=plataformas).values_list('id', flat=True)

        peliculas = pelicula.objects.filter(pelicula_genero__genero_id__in=fil_gen, plataforma_pelicula__plataforma_id__in=fil_plt)
        series = serie.objects.filter(serie_genero__genero_id__in=fil_gen, plataforma_serie__plataforma_id__in=fil_plt)

        gen = genero.objects.all()
        plt = plataforma.objects.all()

        return render(request, 'home_filtros.html', {'header': headerPS,  'generos': gen, 'plataformas': plt, 'peliculas': peliculas, 'series': series})


def guardar_comentario(request):
    if request.method == 'POST':
        id_pelicula = request.POST.get('pelicula_id')
        if request.user.is_authenticated:
            comentario = request.POST.get('comentario_usuario')
            foro = foro_pelicula.objects.get(pelicula_id=id_pelicula)
            nuevo_comentario = comentario_pelicula(contenido=comentario, foro_peliculas_id=foro.id, usuario_id=request.user.id)
            nuevo_comentario.save()
            messages.success(request, '¡Tu comentario ha sido guardado con éxito!')
        else:
            messages.warning(request, 'Debes iniciar sesión para comentar.')

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            messages_html = render_to_string('mensages.html', {'messages': messages.get_messages(request)})
            return JsonResponse({'messages_html': messages_html})

        return redirect('pelicula', id_pelicula=id_pelicula)

def guardar_comentario_serie(request):
    if request.method == 'POST':
        id_serie = request.POST.get('serie_id')
        if request.user.is_authenticated:
            comentario = request.POST.get('comentario_usuario')
            foro = foro_serie.objects.get(serie_id=id_serie)
            nuevo_comentario = comentario_serie(contenido=comentario, foro_series_id=foro.id, usuario_id=request.user.id)
            nuevo_comentario.save()
            messages.success(request, '¡Tu comentario ha sido guardado con éxito!')
        else:
            messages.warning(request, 'Debes iniciar sesión para comentar.')

        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            messages_html = render_to_string('mensages.html', {'messages': messages.get_messages(request)})
            return JsonResponse({'messages_html': messages_html})

        return redirect('serie', id_serie=id_serie)
def crear_foro_peliculas(request):
    contador = 1
    peliculas = pelicula.objects.all()
    for p in peliculas:
        foro = foro_pelicula()
        foro.id = contador
        foro.pelicula_id = p.id
        foro.save()
        contador += 1

    return HttpResponse("Foros agregados")

def crear_foro_series(request):
    contador = 1
    series = serie.objects.all()
    for s in series:
        foro = foro_serie()
        foro.id = contador
        foro.serie_id = s.id
        foro.save()
        contador += 1

    return HttpResponse("Foros agregados")

def buscar(request):
    texto_busqueda = request.GET.get('buscar', '')
    peliculas = pelicula.objects.filter(Q(nombre__icontains=texto_busqueda) | Q(nombre__exact=texto_busqueda))
    series = serie.objects.filter(Q(nombre__icontains=texto_busqueda) | Q(nombre__exact=texto_busqueda))
    return render(request, 'resultado_busqueda.html', {'peliculas': peliculas, 'series': series, 'texto': texto_busqueda})


@login_required()
def cambiar_password(request):
    if request.method == 'POST':
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('password2')
        if new_password != confirm_password:
            messages.add_message(request, messages.WARNING, 'Las contraseñas no coinciden.')
            messages_html = render_to_string('mensages.html', {'messages': messages.get_messages(request)})
            return JsonResponse({'messages_html': messages_html})

        request.user.set_password(new_password)
        request.user.save()
        messages.add_message(request, messages.SUCCESS, 'Cambio de contraseña realizado con existo.')
        messages_html = render_to_string('mensages.html', {'messages': messages.get_messages(request)})
        return JsonResponse({'messages_html': messages_html})

    return render(request, 'reset_password.html')


@login_required()
def usuario_personal(request):
    usu = request.user.usuario_plataforma_set.all()
    plataformas_usuario = [up.plataforma for up in usu]
    contenido_por_plataforma = {}
    for plataforma in plataformas_usuario:
        series_en_plataforma = serie.objects.filter(plataforma_serie__plataforma=plataforma)
        peliculas_en_plataforma = pelicula.objects.filter(plataforma_pelicula__plataforma=plataforma)
        # Calcula la valoración media para cada serie y película
        for s in series_en_plataforma:
            s.valoracion_media = valoracion_serie.objects.filter(serie=s).aggregate(Avg('valoracion'))['valoracion__avg']
        for p in peliculas_en_plataforma:
            p.valoracion_media = valoracion_pelicula.objects.filter(pelicula=p).aggregate(Avg('valoracion'))['valoracion__avg']

        contenido_por_plataforma[plataforma.nombre] = {
                'series': series_en_plataforma,
                'peliculas': peliculas_en_plataforma
            }

    return render(request, 'usuario_personal.html', {'contenido_por_plataforma': contenido_por_plataforma})

def enviar_email_login(request):
    if request.method == 'POST':
        code = random.randint(100000, 999999)
        context = {
            'code': code,
        }
        user_email = request.POST.get('correo_user')
        email_html_message = render_to_string('modelo_email.html', context)
        email = EmailMessage(
            'Codigo de verificación',
            email_html_message,
            'onlywatch.info@gmail.es',
            [user_email],
        )
        email.content_subtype = 'html'
        email.send()
        request.session['verification_code'] = code
        mensaje = "El mesaje ha sido enviado correctamente"
        return JsonResponse({'mensage': mensaje})
    else:
        mensaje = False
        return JsonResponse({'mensage': mensaje})


def filtrar_series(request):
    generos = request.GET.getlist('generos')
    plataformas = request.GET.getlist('plataformas')

    if "Disney " in plataformas:
        plataformas.clear()
        plataformas.append("Disney+")

    if "Moviestar " in plataformas:
        plataformas.clear()
        plataformas.append("Moviestar+")

    if len(generos) == 0:
        fil_plt = plataforma.objects.filter(nombre__in=plataformas).values_list('id', flat=True)
        series = serie.objects.filter(plataforma_serie__plataforma_id__in=fil_plt)

        gen = genero.objects.all()
        plt = plataforma.objects.all()
        return render(request, 'series.html', {'generos': gen, 'plataformas': plt, 'series': series})

    elif len(plataformas) == 0:
        fil_gen = genero.objects.filter(nombre__in=generos).values_list('id', flat=True)
        series = serie.objects.filter(serie_genero__genero_id__in=fil_gen)
        gen = genero.objects.all()
        plt = plataforma.objects.all()
        return render(request, 'series.html', { 'generos': gen, 'plataformas': plt, 'series': series})
    else:
        fil_gen = genero.objects.filter(nombre__in=generos).values_list('id', flat=True)
        fil_plt = plataforma.objects.filter(nombre__in=plataformas).values_list('id', flat=True)

        series = serie.objects.filter(serie_genero__genero_id__in=fil_gen, plataforma_serie__plataforma_id__in=fil_plt)

        gen = genero.objects.all()
        plt = plataforma.objects.all()

        return render(request, 'series.html', { 'generos': gen, 'plataformas': plt, 'series': series})


def filtrar_pelicula(request):
    generos = request.GET.getlist('generos')
    plataformas = request.GET.getlist('plataformas')

    if "Disney " in plataformas:
        plataformas.clear()
        plataformas.append("Disney+")

    if "Moviestar " in plataformas:
        plataformas.clear()
        plataformas.append("Moviestar+")

    if len(generos) == 0:
        fil_plt = plataforma.objects.filter(nombre__in=plataformas).values_list('id', flat=True)
        peliculas = pelicula.objects.filter(plataforma_pelicula__plataforma_id__in=fil_plt)

        gen = genero.objects.all()
        plt = plataforma.objects.all()
        return render(request, 'peliculas.html', {'generos': gen, 'plataformas': plt, 'peliculas': peliculas})
    elif len(plataformas) == 0:
        fil_gen = genero.objects.filter(nombre__in=generos).values_list('id', flat=True)
        peliculas = pelicula.objects.filter(pelicula_genero__genero_id__in=fil_gen)
        gen = genero.objects.all()
        plt = plataforma.objects.all()
        return render(request, 'peliculas.html', {'generos': gen, 'plataformas': plt, 'peliculas': peliculas})
    else:
        fil_gen = genero.objects.filter(nombre__in=generos).values_list('id', flat=True)
        fil_plt = plataforma.objects.filter(nombre__in=plataformas).values_list('id', flat=True)

        peliculas = pelicula.objects.filter(pelicula_genero__genero_id__in=fil_gen, plataforma_pelicula__plataforma_id__in=fil_plt)

        gen = genero.objects.all()
        plt = plataforma.objects.all()

        return render(request, 'peliculas.html', {'generos': gen, 'plataformas': plt, 'peliculas': peliculas})



def add_temporada_json(request):
    with open('static/Temporadas.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Itera sobre cada elemento en los datos
        for d in data:
            tem = temporada()
            tem.nombre = d['nombre']
            tem.sinopsis = d['sinopsis']
            tem.img = d['img']
            tem.fecha_estreno = d['fecha_estreno']
            tem.serie_id = d['serie_id']
            tem.save()
    return HttpResponse("Datos de temporadas cargados correctamente")

def add_episodios_json(request):
    with open('static/Episodios.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        # Itera sobre cada elemento en los datos
        for d in data:
            ep = capitulo()
            ep.nombre = d['nombre']
            ep.numero_capitulo = d['numero_capitulo']
            ep.temporada_id = d['temporada_id']
            ep.save()
    return HttpResponse("Datos de episodios cargados correctamente")


def cargar_datos_sql(request):
    add_series_json()
    add_peliculas_json()
    add_plataformas()
    add_vinculacion_genero_json()
    vinculacion_genero_pelicula_json()
    vinculacion_genero_serie_json()
    vinculacion_plataforma_pelis_json()
    vinculacion_plataforma_series_json()
    add_temporadas_json()
    cargar_actores_personajes(request)
    crear_foro_peliculas(request)
    crear_foro_series(request)
    add_temporada_json(request)
    add_episodios_json(request)
    return HttpResponse("Datos de generos cargados correctamente")


@check_user_role('ADMIN')
def add_uniones_serie(request, id):
    serie_instancia = serie.objects.get(id=id)
    series_generos = serie_instancia.serie_genero_set.all()
    generos_totales = genero.objects.all()
    generos_vinculados = [up.genero for up in series_generos]
    plataformas_totales = plataforma.objects.all()
    serie_plataforma = serie_instancia.plataforma_serie_set.all()
    plataformas_vinculadas = [up.plataforma for up in serie_plataforma]
    actores = actor.objects.all()
    personajes = personaje_serie.objects.filter(serie_id=id)
    if request.method == 'GET':
        return render(request, 'unir_series.html', {'serie': serie_instancia, 'generos': generos_totales ,'genero_vinculado': generos_vinculados, 'plataformas_totales': plataformas_totales, 'plataformas_vinculadas': plataformas_vinculadas,'actores': actor.objects.all(), 'personajes': personajes})
    else:
        return redirect('administracion_home')


@check_user_role('ADMIN')
def vincular_desvincular_genero_serie(request, id):
    genero_id = request.GET.get('generoId')
    # Obtén las instancias completas de la película y el género
    serie_instancia = serie.objects.get(id=id)
    genero_instancia = genero.objects.get(id=genero_id)
    try:
        # Intenta obtener la relación existente entre la película y el género
        gen_pel = serie_genero.objects.get(serie=serie_instancia, genero=genero_instancia)
    except serie_genero.DoesNotExist:
        # Si la relación no existe, se crea
        serie_genero.objects.create(serie=serie_instancia, genero=genero_instancia)
    else:
        # Si la relación existe, se elimina
        gen_pel.delete()
    return redirect('vincular_serie', id=serie_instancia.id)


@check_user_role('ADMIN')
def vincular_desvincular_plataforma_serie(request, id):
    plataformaId = request.GET.get('plataformaId')
    plataforma_instancia = plataforma.objects.get(id=plataformaId)
    try:
        pla_pel = plataforma_serie.objects.get(plataforma=plataforma_instancia, serie=serie.objects.get(id=id))
    except plataforma_serie.DoesNotExist:
        # Si la relación no existe, se crea
        plataforma_serie.objects.create(plataforma=plataforma_instancia, serie=serie.objects.get(id=id))
    else:
        # Si la relación existe, se elimina
        pla_pel.delete()
    return redirect('vincular_serie', id=id)


@check_user_role('ADMIN')
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


@check_user_role('ADMIN')
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


@check_user_role('ADMIN')
def comentario_visivilidad(request, id):
    usuario_instancia = User.objects.get(id=id)
    comentarios_series = comentario_serie.objects.filter(usuario=usuario_instancia)
    comentarios_peliculas = comentario_pelicula.objects.filter(usuario=usuario_instancia)
    if request.method == 'GET':
        return render(request, 'unir_usuarios.html', {'comentarios_series': comentarios_series, 'comentarios_peliculas': comentarios_peliculas,'usuario': usuario_instancia})
    else:
        return redirect('administracion_home')

@check_user_role('ADMIN')
def visivilidad_comentario(request, id):
    cmt = request.GET.get('comentario')
    try:
        comentario = comentario_pelicula.objects.get(id=cmt, usuario_id=id)
        comentario.visibilidad = not comentario.visibilidad  # Cambia el estado de visibilidad
        comentario.save()
    except comentario_pelicula.DoesNotExist:
        return redirect('administracion_home')
    return redirect('coment', id=id)


@check_user_role('ADMIN')
def unir_actor_pelicula(request, id):
    actor_instancia = actor.objects.get(id=id)
    pelicula_id = request.POST.get('peliculaId')
    if request.method == 'POST':
        personaje = request.POST.get('nombre_personaje')
        personaje_pelicula.objects.create(actor=actor_instancia, pelicula_id=pelicula_id, nombre_personaje=personaje)
        return redirect('vincular_pelicula' , id = pelicula_id)
    else:
        return redirect('vincular_pelicula', id = pelicula_id)



@check_user_role('ADMIN')
def eliminar_personaje_pelicula(request, id):
    personaje = personaje_pelicula.objects.get(id=id)
    pelicula_id = personaje.pelicula_id
    personaje.delete()
    return redirect('vincular_pelicula', id=pelicula_id)

@check_user_role('ADMIN')
def unir_actor_serie(request, id):
    actor_instancia = actor.objects.get(id=id)
    serie_id = request.POST.get('serieId')
    if request.method == 'POST':
        personaje = request.POST.get('nombre_personaje')
        personaje_serie.objects.create(actor=actor_instancia, serie_id=serie_id, nombre_personaje=personaje)
        return redirect('vincular_serie' , id = serie_id)
    else:
        return redirect('vincular_serie', id = serie_id)



@check_user_role('ADMIN')
def eliminar_personaje_serie(request, id):
    personaje = personaje_serie.objects.get(id=id)
    serie_id = personaje.serie_id
    personaje.delete()
    return redirect('vincular_serie', id=serie_id)





