from django.conf.urls import url

from apps.login.views import LoginView, LogoutView


urlpatterns = [
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogoutView.as_view(), name='logout'),
]