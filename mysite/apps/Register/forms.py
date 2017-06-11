from django import forms

from apps.catalogo.models import Person

class UserModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
