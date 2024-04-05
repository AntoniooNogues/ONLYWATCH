from static.img import *
import os
from django.core.files import File
from .models import plataforma
from django.http import HttpResponse

def crear_plataforma(request):
    img_dir = 'static/img'  # directory where images are stored
    for filename in os.listdir(img_dir):
        if filename.endswith(".svg"):  # check if the file is an image
            img_path = os.path.join(img_dir, filename)
            with open(img_path, 'rb') as img_file:
                crea = plataforma(nombre=os.path.splitext(filename)[0], img=File(img_file))
                crea.save()
    return HttpResponse("Plataformas creadas")