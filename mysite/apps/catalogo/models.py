from django.db import models
from django.contrib.auth.models import User


#class DefaultModel(models.Model):
 #   usuario_crea = models.ForeignKey(User, help_text='Quien guarda el registro', verbose_name='Usuario que guardo')
  #  creado = models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion del registro', verbose_name='Fecha de creacion')

   # class Meta:
    #    abstract = True


class Nacionalidad(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return "(%s) - %s" % (self.id, self.nombre)


class Person(models.Model):
    GENERO = (
        ('1', 'Hombre'),
        ('2', 'Mujer')
    )
    #state = models.CharField(choices=STATE, max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)
    home_address = models.TextField(null=True, blank=True)
    #birthday = models.DateField()
    genero = models.CharField(choices=GENERO, max_length=10)
    nacionalidad = models.ForeignKey(Nacionalidad)
    facebook = models.CharField(null=True, blank=True, max_length=40)
    twitter = models.CharField(null=True, blank=True, max_length=40)
    #creado = models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion del registro', verbose_name='Fecha de creacion')
    photo = models.ImageField(null=True,  blank=True, upload_to="photos_media")

    def __str__(self):
        return self.first_name

class Articulo(models.Model):
    STATE = (
      ('1', 'Publico'),
      ('2', 'Privado')
    )

    titulo = models.CharField(max_length=40)
    contenido = models.TextField(blank=True)
    #etiqueta =
    state = models.CharField(choices=STATE, max_length=10)
    autor = models.ForeignKey(Person)
    creado = models.DateTimeField(auto_now_add=True, help_text='Fecha de creacion del registro', verbose_name='Fecha de creacion')
    photo = models.ImageField(null=True, upload_to="Articulo_photos_media")

