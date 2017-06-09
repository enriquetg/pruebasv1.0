from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

from braces.views import LoginRequiredMixin

from apps.catalogo.forms import PersonModelForm
from apps.catalogo.models import Person, Nacionalidad

from apps.djangosearchpaginationplus.views import DinamicPaginationMixin, SearchMixin


#from django.core.urlresolver import reverse_lazy

from .genericas import ClaseGenericaDeleteView


class MyFormView(CreateView):
    form_class = PersonModelForm
    template_name = 'myform.html'
    success_url = reverse_lazy('persona-list')



class PersonListView(DinamicPaginationMixin, SearchMixin,  LoginRequiredMixin, ListView):
    model = Person
    template_name = 'milista.html'

    def get_filter(self, queryset):
        busqueda = self.get_search()

        if busqueda:
            queryset = queryset.filter(Q(first_name__icontains=busqueda)|
                            Q(last_name__icontains=busqueda)|
                            Q(nacionalidad__nombre__icontains=busqueda))
        return queryset

    def get_queryset(self):
        numero_paginacion =  self.request.GET.get('rpp', 5)

        numero_pagina = self.request.GET.get('page', 1)

        num_registros = (int (numero_paginacion) * (int(numero_pagina)-1))+1

        entradas = int(numero_paginacion) * int(numero_pagina)

        queryset = super(PersonListView, self).get_queryset()
        total= queryset.count();
        if entradas > total:
            entradas = total

        messages.info(self.request, ('Mostrando '+str(num_registros)+ ' a '+str(entradas)+ ' de %s entradas') %queryset.count())
        return queryset


class PersonaUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'myform.html'
    fields = '__all__'
    model = Person
    success_url = reverse_lazy('persona-list')


class PersonaDeleteView(LoginRequiredMixin, ClaseGenericaDeleteView):
    model = Person


class NacionalidadDeleteView(LoginRequiredMixin, ClaseGenericaDeleteView):
    model = Nacionalidad


class PersonaDetailView(LoginRequiredMixin, DetailView):
    template_name = 'persondetail.html'
    model = Person
    # def get_context_data(self, **kwargs):
    #     context = super(PersonaDetailView, self).get_context_data(**kwargs)
    #     return context


class PersonaTemplateView(TemplateView):
    template_name = 'welcome.html'