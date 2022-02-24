from django import forms
from .models import User, Posts ,comment


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ('name', 'email', 'body')



