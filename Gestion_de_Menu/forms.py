from django import forms
from .models import Plat

class PlatForm(forms.ModelForm):
    class Meta:
        model = Plat
        fields = ['id_plat','nom','categorie','prix','description','image']
