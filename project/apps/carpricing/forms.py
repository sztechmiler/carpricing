import datetime
import re
from six import string_types

from django.utils.dates import MONTHS
from django.utils.safestring import mark_safe

from django import forms
from django.forms.widgets import Widget, Select
from .models import CarBrand, CarModel

class updateForm(forms.Form):
    some_data = forms.CharField(help_text="give me something")


class GetPriceForm(forms.Form):
    Marka = forms.ModelChoiceField(queryset=CarBrand.objects.all(), to_field_name="name", empty_label="Wybierz markę", widget=forms.Select(attrs={'class': 'form-control'}), label="Wymierz markę")
    Model = forms.ChoiceField(choices=(), initial="scos", widget=forms.Select(attrs={'class': 'form-control'}), label="Wybierz model")
    lata =((str(x), x) for x in range(1,32))
    Rok_produkcji = forms.ChoiceField(choices=lata, initial="scos", widget=forms.Select(attrs={'class': 'form-control'}), label="Wybierz model")
    