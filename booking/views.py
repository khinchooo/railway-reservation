from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import Search, Book, Booking
from home.models import RouteStation,Station,Route,Train,Reservation,Payment
import json
import uuid # Required for unique book instances

# Create your views here.
def getTrain(request):
    if request.method=='POST':
        form = Search(request.POST)
        if form.is_valid():
            post_data = form.cleaned_data
            start_station_id = post_data['start_station']
            end_station_id = post_data['end_station']
            data = []
            # for route in routes:
            routestation1 = RouteStation.objects.filter(station_id = end_station_id)
            for i in routestation1:
                train_id = i.train_id
                routestation2 = RouteStation.objects.filter(train_id = train_id, station_id = start_station_id)
                for j in routestation2:
                    if j.order < i.order:
                        data.append(j)
        else:
            return HttpResponse('<h1>Invalid data</h1>')
        return render(request,'home/trains.html', {
            'data': data,
            'start_station': start_station_id,
            'end_station': end_station_id
            })
    return HttpResponse('<h1>Wrong</h1>')

def search(request):
    station = Station.objects.all()
    return render(request,'home/search.html',{'station':station})

def book(request):
    if request.method=='POST':
        form = Book(request.POST)
        if form.is_valid():
            post_data = form.cleaned_data
            route_station_id = post_data['route_station_id']
            no_of_seats = post_data['no_of_seats']
            journey_date = post_data['journey_date']
            print("route_station_id:", route_station_id)
            query_set = RouteStation.objects.filter(id = route_station_id)
            data = query_set.get()
        else:
            return HttpResponse('<h1>Invalid data</h1>')
        return render(request,'home/book.html', {
            'data': data,
            'no_of_seats': no_of_seats,
            'journey_date': journey_date
            })
    return HttpResponse('<h1>Wrong</h1>')

def reserve(request):
    if request.method=='POST':
        form = Booking(request.POST)
        if form.is_valid():
            post_data = form.cleaned_data
            train_name = post_data['train_name']
            train_id = post_data['train_id']
            start_station = post_data['start_station']
            end_station = post_data['end_station']
            no_of_seats = post_data['no_of_seats']
            journey_date = post_data['journey_date']
            reservation_no = uuid.uuid4().hex

            reservation = Reservation()
            reservation.reservation_no = reservation_no
            reservation.train_id = train_id
            reservation.user = "USER"
            reservation.journey_date = journey_date
            reservation.no_of_seats = no_of_seats
            reservation.start_station = start_station
            reservation.end_station = end_station
            reservation.save()
        else:
            return HttpResponse('<h1>Invalid data</h1>')
        return render(request,'home/complete.html', { 'reservation_no': reservation_no })
    return HttpResponse('<h1>Wrong</h1>')
