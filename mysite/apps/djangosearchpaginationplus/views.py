from django.core.exceptions import ImproperlyConfigured
from pure_pagination.mixins import PaginationMixin


class DinamicPaginationMixin(PaginationMixin):
    def get_paginate_by(self, queryset):
        self.paginate_by = self.request.GET.get('rpp', 5)
        if self.paginate_by:
            try:
                self.paginate_by = int(self.paginate_by)
            except ValueError:
                self.paginate_by = 5
        return self.paginate_by

    def get_context_data(self, **kwargs):
        context = super(DinamicPaginationMixin, self).get_context_data(**kwargs)
        context['rpp'] = self.get_paginate_by(self.queryset)
        return context


class SearchMixin(object):

    def get_search(self):
        return self.request.GET.get('search', '')

    def get_filter(self, queryset):
        raise ImproperlyConfigured('Debe especificar implementar el filtro de busqueda')

    def get_queryset(self):
        queryset = super(SearchMixin, self).get_queryset()
        queryset = self.get_filter(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context= super(SearchMixin, self).get_context_data(**kwargs)
        context['search'] = self.get_search()
        return context