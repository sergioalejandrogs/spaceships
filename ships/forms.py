from django import forms
from .models import Ship

class ShipForm(forms.ModelForm):
    class Meta:
        model = Ship
        fields = '__all__'
