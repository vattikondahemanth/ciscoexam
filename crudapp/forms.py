from django import forms
from .models import CiscoModel

class CiscoForm(forms.ModelForm):
    class Meta:
        model = CiscoModel
        fields = "__all__"
