from django import forms
from area_usuario.models import Projetos


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projetos
        fields = ['projeto']