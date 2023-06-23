from django import forms
from .models import Bay

class ChoiceForm(forms.ModelForm):
    class Meta:
     model = Bay
     exclude = ['product']
     fields = '__all__'