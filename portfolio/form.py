from django import forms
from .models import Portfolio

class Post(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'image', 'description']

        