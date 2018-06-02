from django import forms
from .models import Word

class wordForm(forms.Form):
    id=forms.IntegerField()
    name=forms.CharField()
    kullanici=forms.CharField()

class kullaniciForm(forms.Form):
    userName=forms.CharField()
    password=forms.CharField()

class meanForm(forms.Form):
    meanName=forms.CharField()
    word=forms.CharField()