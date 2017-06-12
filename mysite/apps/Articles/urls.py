from django.conf.urls import url

from apps.Register.views import Register, UserDetailView, UserListView, UserUpdateView, UserDeleteView
#   PersonaTemplateView

# from apps.catalogo.views import PersonaDetailView

urlpatterns = [
    url(r'^persona/list$', UserListView.as_view(), name='user-list'),
    url(r'^persona/register$', Register.as_view(), name='user-add'),
    url(r'^persona/update/(?P<pk>[0-9]+)/$', UserUpdateView.as_view(), name='user-update'),
    url(r'^persona/delete/(?P<pk>[0-9]+)/$', UserDeleteView.as_view(), name='user-delete'),
    url(r'^persona/detail/(?P<pk>[0-9]+)/$', UserDetailView.as_view(), name='user-detail'),
    #url(r'^persona/welcome$', PersonaTemplateView.as_view(), name='welcome'),
]
