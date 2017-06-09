from django.conf.urls import url

#from apps.views import myform
from apps.catalogo.views import MyFormView, PersonListView, PersonaUpdateView, PersonaDeleteView, PersonaDetailView, NacionalidadDeleteView, PersonaTemplateView

# from apps.catalogo.views import PersonaDetailView

urlpatterns = [
    url(r'^persona/list$', PersonListView.as_view(), name='persona-list'),
    url(r'^persona/add$', MyFormView.as_view(), name='persona-add'),
    url(r'^persona/update/(?P<pk>[0-9]+)/$', PersonaUpdateView.as_view(), name='persona-update'),
    url(r'^nacionalidad/delete/(?P<pk>[0-9]+)/$', NacionalidadDeleteView.as_view(), name='nacionalidad-eliminar'),
    url(r'^persona/delete/(?P<pk>[0-9]+)/$', PersonaDeleteView.as_view(), name='persona-delete'),
    url(r'^persona/detail/(?P<pk>[0-9]+)/$', PersonaDetailView.as_view(), name='persona-detail'),
    url(r'^persona/welcome$', PersonaTemplateView.as_view(), name='persona-welcome'),
]
