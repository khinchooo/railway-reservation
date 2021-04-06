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

class AddTrain(forms.Form):
    train_id = forms.CharField(max_length=50)
    train_name = forms.CharField(max_length=50)
    route_id = forms.CharField(max_length=50)

class AddRoute(forms.Form):
    route_id = forms.CharField(max_length=50)
    start_station = forms.CharField(max_length=50)
    end_station = forms.CharField(max_length=50)

class AddStation(forms.Form):
    station_id = forms.CharField(max_length=50)
    station_name = forms.CharField(max_length=50)

class AddRouteTrain(forms.Form):
    train_id = forms.CharField(max_length=50)
    station_id = forms.CharField(max_length=50)
    route_id = forms.CharField(max_length=50)
    order = forms.IntegerField()
    departure_time = forms.TimeField()
    arrival_time = forms.TimeField()
    