from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

from braces.views import LoginRequiredMixin

from apps.catalogo.forms import PersonModelForm, ArticuloModelForm
from apps.catalogo.models import Profile, Articulo
from apps.djangosearchpaginationplus.views import DinamicPaginationMixin, SearchMixin


from .genericas import ClaseGenericaDeleteView

class ArticuloListeView(DinamicPaginationMixin,LoginRequiredMixin, ListView):
    model = Articulo
    template_name = 'catalogo/milista_articulo.html'


class AddArticuloView(LoginRequiredMixin, CreateView):
    form_class = ArticuloModelForm
    template_name = 'catalogo/addarticulo.html'
    success_url = reverse_lazy('articuloo-lista')


class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'catalogo/addarticulo.html'
    fields = '__all__'
    model = Articulo
    success_url = reverse_lazy('articuloo-lista')


class ArticuloDeleteView(LoginRequiredMixin, ClaseGenericaDeleteView):
    model = Articulo
    template_name = 'generic/confirm_delete.html'
    success_url = reverse_lazy('articuloo-lista')


class ArticuloDetailView(LoginRequiredMixin, DetailView):
    template_name = 'catalogo/articulodetail.html'
    model = Articulo


class MyFormView(LoginRequiredMixin, CreateView):
    form_class = PersonModelForm
    template_name = 'catalogo/myform.html'
    success_url = reverse_lazy('persona-list')

from django.contrib import admin

class PersonListView(LoginRequiredMixin, ListView):
    model = admin
    template_name = 'catalogo/milista.html'


class PersonaUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'catalogo/myform.html'
    fields = '__all__'
    model = Profile
    success_url = reverse_lazy('persona-list')


class PersonaDeleteView(LoginRequiredMixin, ClaseGenericaDeleteView):
     model = Profile



class PersonaDetailView(LoginRequiredMixin, DetailView):
    template_name = 'catalogo/persondetail.html'
    model = Profile


class PersonaTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'catalogo/welcome.html'