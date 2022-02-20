from django import forms
from .models import *


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = "__all__"