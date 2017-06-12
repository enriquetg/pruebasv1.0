from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

from apps.catalogo.forms import PersonModelForm
from apps.catalogo.models import Profile, Articulo

from apps.djangosearchpaginationplus.views import DinamicPaginationMixin, SearchMixin


class BlogListView(DinamicPaginationMixin, SearchMixin, ListView):
    model = Articulo
    template_name = 'blog/milista.html'

    def get_filter(self, queryset):
        busqueda = self.get_search()

        if busqueda:
            queryset = queryset.filter(Q(titulo__icontains=busqueda))
                           # Q(autor__last_name__icontains=busqueda))
        return queryset

    def get_queryset(self):
        numero_paginacion =  self.request.GET.get('rpp', 5)
        numero_pagina = self.request.GET.get('page', 1)
        num_registros = (int (numero_paginacion) * (int(numero_pagina)-1))+1
        entradas = int(numero_paginacion) * int(numero_pagina)
        queryset = super(BlogListView, self).get_queryset()
        total= queryset.count();
        if entradas > total:
            entradas = total
            messages.info(self.request, ('Mostrando '+str(num_registros)+ ' a '+str(entradas)+ ' de %s entradas') %queryset.count())
        return queryset


class BlogDetailView( DetailView):
            template_name = 'blog/blogdetail.html'
            model = Articulo

            def get_context_data(self, **kwargs):
                context = super(BlogDetailView, self).get_context_data(**kwargs)
                return context


class PersonaaDetailView(DetailView):
    template_name = 'blog/persondetalle.html'
    model = Profile