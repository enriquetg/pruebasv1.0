from django.contrib import admin
from apps.catalogo.models import Person, Nacionalidad, Articulo, Profile
from reversion.admin import VersionAdmin

@admin.register(Person)
class MyModelAdmin(VersionAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(VersionAdmin):
    pass


@admin.register(Nacionalidad)
class NacionalidadAdmin(VersionAdmin):
    pass


@admin.register(Articulo)
class ArticuloAdmin(VersionAdmin):
    pass

