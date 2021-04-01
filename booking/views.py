from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import Search
from home.models import RouteStation, Station
import json
# Create your views here.
def getTrain(request):
    if request.method=='POST':
        form = Search(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            start_station = ['start_station']
            end_station = ['end_station']
            routestation1 = RouteStation.objects.filter(station_id = end_station)
            data = []
            o = 0
            for i in routestation1:
                train_no = i.train_no
                routestation2 = RouteStation.objects.filter(train_no = train_no, station_id = start_station)               
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

def book1(request):
    if(redirect.method=='POST'):
        date = request.POST('date')
        start = request.POST('star_station')
        end = request.POST('end_station')
        train = request.POST('bk')
        seat = request.POST['classes' + str(train_no)]
        nos = request.POST['booking_no'+str(tno)]
        price = request.POST['price'+str(tno)]
        tname=Train.objects.get(train_no = train_no).train_name
        return render(request,'features/payment.html',{'price':int(pr)*int(nos),'dt':dt,'cls':cls,'tno':tno,'nos':nos,'tname':tname,'src':src,'des':des})
