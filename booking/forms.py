from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class Search(forms.Form):
    start_station = forms.CharField(max_length=50)
    end_station = forms.CharField(max_length=50)

class Book(forms.Form):
    route_station_id = forms.IntegerField()
    no_of_seats = forms.IntegerField()
    journey_date = forms.DateField()
    start_station = forms.CharField(max_length=50)
    end_station = forms.CharField(max_length=50)

class Booking(forms.Form):
    train_name = forms.CharField(max_length=50)
    train_id = forms.CharField(max_length=50)
    start_station = forms.CharField(max_length=50)
    end_station = forms.CharField(max_length=50)
    no_of_seats = forms.IntegerField()
    journey_date = forms.DateField()

class Cancel(forms.Form):
    reservation_id = forms.IntegerField()
    