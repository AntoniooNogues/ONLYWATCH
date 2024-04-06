from django.db import models
from django.utils import timezone


# Create your models here.
class plataforma(models.Model):
    nombre = models.CharField(max_length=50)
    img = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.nombre}  {self.img}"

class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100, default=" ")
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=100, default="")
    tipo = models.IntegerField(default=2)
    img = models.CharField(max_length=300)
    fecha_nacimiento = models.DateField(null=True)
    sexo = models.CharField(max_length=25, default="NS/NC")

    def __str__(self):
        return f"{self.nombre} {self.apellidos} {self.email} {self.img}"

class serie(models.Model):
    nombre = models.CharField(max_length=100)
    sinopsis = models.TextField()
    img = models.CharField(max_length=300)
    trailer = models.CharField(max_length=300)
    director = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.img+" "+self.trailer+" "+self.director

class genero(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    def __str__(self):
        return self.nombre + " " + self.descripcion

class actor(models.Model):
    nombre = models.CharField(max_length=50)
    img = models.CharField(max_length=300)
    def __str__(self):
        return self.nombre + " " + self.img
class pelicula(models.Model):
    nombre = models.CharField(max_length=50)
    sinopsis = models.TextField()
    fecha_estreno = models.DateField()
    img = models.CharField(max_length=300)
    url_trailer = models.CharField(max_length=300)
    director = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre + " " + self.sinopsis + " " + self.fecha_estreno+ " " + self.img + " " + self.url_trailer + " " + self.director

class foro_serie(models.Model):
    serie = models.ForeignKey(serie, on_delete=models.CASCADE)

    def __str__(self):
        return self.serie
class foro_pelicula(models.Model):
    pelicula = models.ForeignKey(pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return self.pelicula

class comentario_serie(models.Model):
    contenido = models.CharField(max_length=500)
    visibilidad = models.BooleanField(default=True)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    foro_series = models.ForeignKey(foro_serie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.usuario.nombre) + ": " + self.contenido
class comentario_pelicula(models.Model):
    contenido = models.CharField(max_length=500)
    visibilidad = models.BooleanField(default=True)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    foro_peliculas = models.ForeignKey(foro_pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.nombre + ": " + self.contenido

class respuestas_series(models.Model):
    contenido = models.CharField(max_length=500)
    visibilidad = models.BooleanField(default=True)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    comentario_series = models.ForeignKey(comentario_serie, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario+ ": " + self.contenido

class respuestas_peliculas(models.Model):
    contenido = models.CharField(max_length=500)
    visibilidad = models.BooleanField(default=True)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    comentario_peliculas = models.ForeignKey(comentario_pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario+ ": " + self.contenido

class temporada(models.Model):
    nombre = models.CharField(max_length=100)
    sinopsis = models.TextField()
    img = models.CharField(max_length=300)
    fecha_estreno = models.DateField()
    serie = models.ForeignKey(serie, on_delete=models.CASCADE)

    def __str__(self):
        return self.img + " "+self.nombre + " " + self.sinopsis + " " + self.fecha_estreno

class capitulo(models.Model):
    nombre = models.CharField(max_length=100)
    sinopsis = models.TextField()
    img = models.CharField(max_length=300)
    fecha_estreno = models.DateField()
    temporada = models.ForeignKey(temporada, on_delete=models.CASCADE)

    def __str__(self):
        return self.img + " "+self.nombre + " " + self.sinopsis + " " + self.url

class valoracion_serie(models.Model):
    valoracion = models.IntegerField(null=True)
    estado = models.IntegerField(null=True)
    ultimo_capitulo = models.IntegerField(null=True)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    serie = models.ForeignKey(serie, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario + " " + self.serie + " " + self.valoracion + " " + self.estado + " " + self.ultimo_capitulo

class valoracion_pelicula(models.Model):
    valoracion = models.IntegerField(null=True)
    estado = models.IntegerField(null=True)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario + " " + self.pelicula + " " + self.valoracion + " " + self.estado

class peliculas_favoritas(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario + " " + self.pelicula
class series_favoritas(models.Model):
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    serie = models.ForeignKey(serie, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario + " " + self.serie

class plataforma_pelicula(models.Model):
    plataforma = models.ForeignKey(plataforma, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return self.plataforma + " " + self.pelicula

class plataforma_serie(models.Model):
    plataforma = models.ForeignKey(plataforma, on_delete=models.CASCADE)
    serie = models.ForeignKey(serie, on_delete=models.CASCADE)

    def __str__(self):
        return self.plataforma + " " + self.serie

class personaje_pelicula(models.Model):
    nombre_personaje = models.CharField(max_length=50)
    actor = models.ForeignKey(actor, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_personaje + " " + self.actor.nombre + " " + self.pelicula

class personaje_serie(models.Model):
    nombre_personaje = models.CharField(max_length=50)
    actor = models.ForeignKey(actor, on_delete=models.CASCADE)
    serie = models.ForeignKey(serie, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_personaje + " " + self.actor.nombre + " " + self.serie

class pelicula_genero(models.Model):
    genero = models.ForeignKey(genero, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return self.genero + " " + self.pelicula

class serie_genero(models.Model):
    genero = models.ForeignKey(genero, on_delete=models.CASCADE)
    serie = models.ForeignKey(serie, on_delete=models.CASCADE)

    def __str__(self):
        return self.genero + " " + self.serie
