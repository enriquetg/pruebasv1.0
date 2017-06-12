from django.conf.urls import url

from apps.catalogo.views import MyFormView, PersonListView, PersonaUpdateView, PersonaDeleteView, PersonaDetailView, PersonaTemplateView,ArticuloListeView, AddArticuloView, ArticuloUpdateView, ArticuloDeleteView, ArticuloDetailView



urlpatterns = [
    url(r'^persona/list$', PersonListView.as_view(), name='persona-list'),
    url(r'^articulo/list$', ArticuloListeView.as_view(), name='articuloo-lista'),
    url(r'^articulo/add$', AddArticuloView.as_view(), name='articulo-add'),
    url(r'^articulo/update/(?P<pk>[0-9]+)/$', ArticuloUpdateView.as_view(), name='articulo-update'),
    url(r'^persona/delete/(?P<pk>[0-9]+)/$', ArticuloDeleteView.as_view(), name='articulo-delete'),
    url(r'^persona/detail/(?P<pk>[0-9]+)/$', ArticuloDetailView.as_view(), name='articulo-detail'),


    url(r'^persona/add$', MyFormView.as_view(), name='persona-add'),
    url(r'^persona/update/(?P<pk>[0-9]+)/$', PersonaUpdateView.as_view(), name='persona-update'),
    url(r'^persona/delete/(?P<pk>[0-9]+)/$', PersonaDeleteView.as_view(), name='persona-delete'),
    url(r'^persona/detail/(?P<pk>[0-9]+)/$', PersonaDetailView.as_view(), name='persona-detail'),
    url(r'^persona/welcome$', PersonaTemplateView.as_view(), name='persona-welcome'),
]
