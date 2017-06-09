from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.login.urls')),
    url(r'^catalogo/', include('apps.catalogo.urls')),
]
