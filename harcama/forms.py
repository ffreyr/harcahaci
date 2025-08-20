from django import forms
from .models import Harcama

class HarcamaForm(forms.ModelForm):
    class Meta:
        model = Harcama
        fields = ['amount', 'description', 'category']