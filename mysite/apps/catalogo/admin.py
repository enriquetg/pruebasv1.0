from django.contrib import admin
from apps.catalogo.models import Person, Nacionalidad
from reversion.admin import VersionAdmin


@admin.register(Person)
class MyModelAdmin(VersionAdmin):
    pass


@admin.register(Nacionalidad)
class NacionalidadAdmin(VersionAdmin):
    pass
