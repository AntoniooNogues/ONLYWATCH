from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
# Create your models here.
class plataforma(models.Model):
    nombre = models.CharField(max_length=50)
    img = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.nombre}  {self.img}"

class Rol(models.TextChoices):
    ADMINISTRADOR = 'ADMIN', 'Administrador'
    USUARIO = 'USUARIO', 'Usuario'


class UserManager(BaseUserManager):
    def create_user(self,  email, password=None, **extra_fields):
        if not email:
            raise ValueError('El usuario debe tener un email')
        email = self.normalize_email(email)
        user = self.model(email=email,  **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True.')
        return self.create_user(email, password, **extra_fields)



class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    nombre_completo = models.CharField(max_length=150, null=True)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField(null=True)
    img = models.CharField(max_length=300, null=True)
    sexo = models.CharField(max_length=25, default="NS/NC", null=True)
    rol = models.CharField(max_length=50, choices=Rol.choices, default=Rol.USUARIO)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email']


    def __str__(self):
        return self.username

class serie(models.Model):
    nombre = models.CharField(max_length=100)
    sinopsis = models.TextField()
    img = models.CharField(max_length=300)
    fecha_estreno = models.DateField()
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
        return f"{self.nombre} {self.sinopsis} {self.fecha_estreno} {self.img} {self.url_trailer} {self.director}"

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
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    foro_series = models.ForeignKey(foro_serie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.usuario.username) + ": " + self.contenido
class comentario_pelicula(models.Model):
    contenido = models.CharField(max_length=500)
    visibilidad = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    foro_peliculas = models.ForeignKey(foro_pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.usuario.username) + ": " + self.contenido

class respuestas_series(models.Model):
    contenido = models.CharField(max_length=500)
    visibilidad = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario_series = models.ForeignKey(comentario_serie, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.usuario.username) + ": " + self.contenido

class respuestas_peliculas(models.Model):
    contenido = models.CharField(max_length=500)
    visibilidad = models.BooleanField(default=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario_peliculas = models.ForeignKey(comentario_pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.usuario.username)+ ": " + self.contenido

class temporada(models.Model):
    nombre = models.CharField(max_length=100)
    sinopsis = models.TextField()
    img = models.CharField(max_length=300)
    fecha_estreno = models.DateField()
    serie = models.ForeignKey(serie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.serie} {self.nombre} {self.sinopsis} {self.img} {self.fecha_estreno}"

class capitulo(models.Model):
    nombre = models.CharField(max_length=100)
    sinopsis = models.TextField()
    img = models.CharField(max_length=300)
    fecha_estreno = models.DateField()
    temporada = models.ForeignKey(temporada, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.temporada} {self.nombre} {self.sinopsis} {self.img} {self.fecha_estreno}"

class valoracion_serie(models.Model):
    valoracion = models.IntegerField(null=True)
    estado = models.IntegerField(null=True)
    ultimo_capitulo = models.IntegerField(null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    serie = models.ForeignKey(serie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} {self.serie} {self.valoracion} {self.estado} {self.ultimo_capitulo}"

class valoracion_pelicula(models.Model):
    valoracion = models.IntegerField(null=True)
    estado = models.IntegerField(null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} {self.pelicula} {self.valoracion} {self.estado}"

class peliculas_favoritas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} {self.pelicula}"
class series_favoritas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    serie = models.ForeignKey(serie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.username} {self.serie}"

class plataforma_pelicula(models.Model):
    plataforma = models.ForeignKey(plataforma, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.plataforma} {self.pelicula}"

class plataforma_serie(models.Model):
    plataforma = models.ForeignKey(plataforma, on_delete=models.CASCADE)
    serie = models.ForeignKey(serie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.plataforma} {self.serie}"

class personaje_pelicula(models.Model):
    nombre_personaje = models.CharField(max_length=50)
    actor = models.ForeignKey(actor, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.actor.nombre} {self.nombre_personaje} {self.pelicula}"

class personaje_serie(models.Model):
    nombre_personaje = models.CharField(max_length=50)
    actor = models.ForeignKey(actor, on_delete=models.CASCADE)
    serie = models.ForeignKey(serie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.actor.nombre} {self.nombre_personaje}  {self.serie}"

class pelicula_genero(models.Model):
    genero = models.ForeignKey(genero, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(pelicula, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.genero} {self.pelicula}"

class serie_genero(models.Model):
    genero = models.ForeignKey(genero, on_delete=models.CASCADE)
    serie = models.ForeignKey(serie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.genero} {self.serie}"
