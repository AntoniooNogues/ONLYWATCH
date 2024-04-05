from static.img import *
import os
from django.core.files import File
from .models import *
from django.http import HttpResponse
from django.db import connection


"""def crear_plataforma(request):
    img_dir = 'static/img'  # directory where images are stored
    for filename in os.listdir(img_dir):
        if filename.endswith(".svg"):  # check if the file is an image
            img_path = os.path.join(img_dir, filename)
            with open(img_path, 'rb') as img_file:
                crea = plataforma(nombre=os.path.splitext(filename)[0], img=File(img_file))
                crea.save()
    return HttpResponse("Plataformas creadas")"""

def crear_serie(request):
    serie1 = serie(nombre="The Witcher", sinopsis="Geralt de Rivia, un cazador de monstruos solitario, lucha por encontrar su lugar en un mundo donde las personas a menudo son más malvadas que las bestias.", img="https://pics.filmaffinity.com/the_witcher-737807462-mmed.jpg", trailer="https://www.youtube.com/watch?v=ndl1W4ltcmg", director="Lauren Schmidt Hissrich")
    serie1.save()
    serie2 = serie(nombre="The Mandalorian", sinopsis="The Mandalorian es una serie de televisión web de espacio occidental estadounidense que se estrenó en Disney+ el 12 de noviembre de 2019. Ambientada en el universo de Star Wars, la serie tiene lugar cinco años después de los eventos de El retorno del Jedi y sigue a un pistolero solitario más allá de los límites de la Nueva República.", img="https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTE5IGVtPm4r5jG-dlf9tQ2Ymc8wu-CgsiaVu2M9VL4_3s0XJd8", trailer="https://www.youtube.com/watch?v=eW7Twd85m2g", director="Jon Favreau")
    serie2.save()
    serie3 = serie(nombre="Breaking Bad", sinopsis="Breaking Bad es una serie de televisión dramática estadounidense creada y producida por Vince Gilligan. La serie se estrenó el 20 de enero de 2008 en la cadena de televisión por cable AMC y finalizó el 29 de septiembre de 2013. Se conoce por su personaje principal, Walter White, un profesor de química de secundaria que se convierte en un narcotraficante después de ser diagnosticado con cáncer de pulmón.", img="https://m.media-amazon.com/images/M/MV5BYmQ4YWMxYjUtNjZmYi00MDQ1LWFjMjMtNjA5ZDdiYjdiODU5XkEyXkFqcGdeQXVyMTMzNDExODE5._V1_.jpg", trailer="https://www.youtube.com/watch?v=HhesaQXLuRY", director="Vince Gilligan")
    serie3.save()
    return HttpResponse(f"Serie creada")