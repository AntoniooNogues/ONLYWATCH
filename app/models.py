from django.db import models

# Create your models here.
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
