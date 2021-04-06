from django.db import models

# Create your models here.
class Train(models.Model):
    train_id = models.CharField(primary_key=True,max_length=50)
    train_name = models.CharField(max_length=50)
    route = models.ForeignKey('Route',on_delete=models.CASCADE)

    def __str__(self):
        return self.train_id

class Route(models.Model):
    route_id = models.CharField(max_length=50)
    start_station = models.CharField(max_length=50)
    end_station = models.CharField(max_length=50)
    def __str__(self):
        return self.route_id

class Station(models.Model):
    station_id = models.CharField(primary_key=True,max_length=50)
    station_name = models.CharField(max_length=50)
    def __str__(self):
        return self.station_id

class RouteStation(models.Model):
    train = models.ForeignKey('Train',on_delete=models.CASCADE)
    station = models.ForeignKey('Station',on_delete=models.CASCADE)
    route = models.ForeignKey('Route',on_delete=models.CASCADE)
    order = models.IntegerField()
    departure_time = models.TimeField(null=True, blank=True)
    arrival_time = models.TimeField(null=True, blank=True)

class Reservation(models.Model):
    reservation_no = models.CharField(max_length=32, null=True, blank=True)
    train = models.ForeignKey('Train',on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    journey_date = models.DateField(null=True, blank=True)
    no_of_seats = models.CharField(max_length=50)
    start_station = models.CharField(max_length=50)
    end_station = models.CharField(max_length=50)
