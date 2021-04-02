from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import Search, AddTrain
from home.models import RouteStation,Station,Route,Train,Reservation,Payment
import json
# Create your views here.
def getTrain(request):
    if request.method=='POST':
        form = Search(request.POST)
        if form.is_valid():
            post_data = form.cleaned_data
            start_station = post_data['start_station']
            end_station = post_data['end_station']

            routestation1 = RouteStation.objects.filter(station_id = end_station)
            data = []
            o = 0
            for i in routestation1:
                train_id = i.train_id
                routestation2 = RouteStation.objects.filter(train_id = train_id, station_id = start_station)               
                for j in routestation2:
                    if j.order < i.order:
                        data.append(j)
                        o = i.order-j.order
        else:
            return HttpResponse('<h1>Invalid data</h1>')
        return render(request,'booking/trains.html',{'data':data,'o':o,'start_station':start_station,'end_station':end_station})
    return HttpResponse('<h1>Wrong</h1>')

def search(request):
    station = Station.objects.all()
    return render(request,'booking/search.html',{'station':station})