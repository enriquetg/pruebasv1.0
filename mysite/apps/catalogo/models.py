from django.db import models


class Nacionalidad(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return "(%s) - %s" % (self.id, self.nombre)


class Person(models.Model):
    GENERO = (
        ('1', 'Hombre'),
        ('2', 'Mujer')
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)
    home_address = models.TextField(null=True, blank=True)
    birthday = models.DateField()
    genero = models.CharField(choices=GENERO, max_length=10)
    nacionalidad = models.ForeignKey(Nacionalidad)

    def __str__(self):
        return self.first_name
