from django.views.generic import FormView, View, CreateView, DetailView
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

class LoginView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        link = self.request.GET.get('next', "/catalogo/persona/welcome")
        #link = self.request.GET.get('next', "/catalogo/persona/list")

        form = self.get_form()

        if form.is_valid():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                l = login(request, user)
                return HttpResponseRedirect(link)
            else:
                print('usuario no encontrado')
                return HttpResponseRedirect({request.path})
        else:
            return HttpResponseRedirect(request.path)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/accounts/login/')

