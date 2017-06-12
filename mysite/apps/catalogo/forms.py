from django import forms

from apps.catalogo.models import Person
# class MyForm(forms.Form):
#     nombre = forms.CharField(label='Nombre', max_length=100)
#     paterno = forms.CharField(label='A. Paterno', max_length=100)
#     correo = forms.EmailField(label='Email')

class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
