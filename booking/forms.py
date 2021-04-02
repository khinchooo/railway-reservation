from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class AddTrain(forms.Form):
    route_id = forms.CharField(max_length=50)
    train_id = forms.CharField(max_length=50)
    train_name = forms.CharField(max_length=50)

class Search(forms.Form):
    start_station = forms.CharField(max_length=50)
    end_station = forms.CharField(max_length=50)