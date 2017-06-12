from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, FormView, TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q

from braces.views import LoginRequiredMixin
from .genericas import ClaseGenericaDeleteView

from apps.Register.forms import UserModelForm
from apps.catalogo.models import Profile

from apps.djangosearchpaginationplus.views import DinamicPaginationMixin, SearchMixin


class Register(CreateView):
    form_class = UserModelForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('user-list')


class UserDetailView(DetailView):
    template_name = 'register/persondetail.html'
    model = Profile
    def get_context_data(self, **kwargs):
         context = super(UserDetailView, self).get_context_data(**kwargs)
         return context


class UserListView(DinamicPaginationMixin, SearchMixin,  LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'register/milista.html'

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

        queryset = super(UserListView, self).get_queryset()
        total= queryset.count();
        if entradas > total:
            entradas = total

        messages.info(self.request, ('Mostrando '+str(num_registros)+ ' a '+str(entradas)+ ' de %s entradas') %queryset.count())
        return queryset


class UserUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'register/register.html'
    fields = '__all__'
    model = Profile
    success_url = reverse_lazy('user-list')


class UserDeleteView(LoginRequiredMixin, ClaseGenericaDeleteView):
    model = Profile


#class PersonaTemplateView(TemplateView):
 #   template_name = 'welcome.html'