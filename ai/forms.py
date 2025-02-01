from django import forms
from .models import Ai

class AiForm(forms.ModelForm):
    
    class Meta:
        model = Ai
        fields = ["question"]