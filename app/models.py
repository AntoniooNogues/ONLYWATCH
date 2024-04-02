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
    trailer = models.CharField(max_length=300)
    director = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+self.img+" "+self.trailer+" "+self.director