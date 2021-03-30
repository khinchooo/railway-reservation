from django.db import models

# Create your models here.
class Train(models.Model):
    train_no = models.CharField(primary_key=True,max_length=50)
    train_name = models.CharField(max_length=50)
    route_no = models.ForeignKey('Route',on_delete=models.CASCADE)

    def __str__(self):
        return self.train_no

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
    train_no = models.ForeignKey('Train',on_delete=models.CASCADE)
    station_id = models.ForeignKey('Station',on_delete=models.CASCADE)
    route_id = models.ForeignKey('Route',on_delete=models.CASCADE)
    order = models.IntegerField()
    departure_time = models.TimeField(null=True, blank=True)
    arrival_time = models.TimeField(null=True, blank=True)

class Reservation(models.Model):
    train_no = models.ForeignKey('Train',on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    booking_no = models.IntegerField()
    booking_date = models.DateField(null=True, blank=True)
    amount = models.IntegerField()
    train_classes = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    pessanger_record = models.CharField(max_length=50)
    start_station = models.CharField(max_length=50)
    end_station = models.CharField(max_length=50)

class Payment(models.Model):
    pessanger_record = models.CharField(max_length=50)
    user = models.CharField(max_length=50)
    amount = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateField(null=True, blank=True)
    cancel = models.CharField(max_length=50)
