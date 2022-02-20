from django import forms
from .models import User, Posts


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"



