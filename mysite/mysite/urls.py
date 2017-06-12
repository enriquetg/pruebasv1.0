from django.conf.urls import url, include, static
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('apps.login.urls')),
    url(r'^blog/', include('apps.Blog.urls')),
    url(r'^catalogo/', include('apps.catalogo.urls')),
    url(r'^register/', include('apps.Register.urls')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
