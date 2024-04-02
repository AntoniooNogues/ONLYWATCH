from django.db import models

# Create your models here.

class plataforma(models.Model):
    nombre = models.CharField(max_length=50)
    img = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre+" "+self.img

class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    tipo = models.IntegerField()
    img = models.CharField(max_length=300)

    def __str__(self):
        return self.nombre+" "+self.img

class serie(models.Model):
    nombre = models.CharField(max_length=100)
    sinopsis = models.TextField()
    img = models.CharField(max_length=300)
    url_trailer = models.CharField(max_length=300)
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
        return self.usuario+ ": " + self.contenido
class comentario_pelicula(models.Model):
    contenido = models.CharField(max_length=500)
    visibilidad = models.BooleanField(default=True)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    foro_peliculas = models.ForeignKey(foro_pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario+ ": " + self.contenido

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
    valoracion = models.IntegerField(default=null)
    estado = models.IntegerField(default=null)
    ultimo_capitulo = models.IntegerField(default=null)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    serie = models.ForeignKey(serie, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario + " " + self.serie + " " + self.valoracion + " " + self.estado + " " + self.ultimo_capitulo

class valoracion_pelicula(models.Model):
    valoracion = models.IntegerField(default=null)
    estado = models.IntegerField(default=null)
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario + " " + self.pelicula + " " + self.valoracion + " " + self.estado