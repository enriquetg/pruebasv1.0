from django.conf.urls import url

from apps.Blog.views import BlogListView, BlogDetailView, PersonaaDetailView

urlpatterns = [
    url(r'^list/', BlogListView.as_view(), name='blog-list'),
    url(r'^articulo/detail/(?P<pk>[0-9]+)/$', BlogDetailView.as_view(), name='blogg-detail'),
    url(r'^autor/detail/(?P<pk>[0-9]+)/$',PersonaaDetailView.as_view(), name='autor-detail'),

]
