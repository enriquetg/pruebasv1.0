from django import forms

from apps.catalogo.models import Profile

class UserModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
