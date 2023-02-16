from django import forms
from .models import Abonent


class AbonentForm(forms.ModelForm):
    class Meta:
        model = Abonent
        exclude = ['created_date']