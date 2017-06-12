from django.urls import reverse_lazy
from django.views.generic import DeleteView


class ClaseGenericaDeleteView(DeleteView):
    template_name = 'generic/confirm_delete.html'
    success_url = reverse_lazy('persona-list')

