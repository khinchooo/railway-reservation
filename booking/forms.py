from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class Search(forms.Form):
    start_station = forms.CharField(max_length=50)
    end_station = forms.CharField(max_length=50)