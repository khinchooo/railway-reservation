from django.contrib import admin
from .models import Train,Route,Station,RouteStation,Reservation

# Register your models here.
admin.site.register(Train)
admin.site.register(Route)
admin.site.register(Station)
admin.site.register(RouteStation)
admin.site.register(Reservation)