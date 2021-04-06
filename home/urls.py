from django.contrib import admin
from django.urls import path
import booking
from . import views
app_name='booking'
urlpatterns = [
    path('', views.Home, name="booking" ),
    path('logout', views.logout),
    path('search/', booking.views.search),
    path('trains', booking.views.getTrain),
    path('book', booking.views.book),
    path('reserve', booking.views.reserve),
    path('cancel', booking.views.cancel),
    path('addTrain/',booking.views.addTrain),
    path('addStation/',booking.views.addStation),
    path('addRoute/',booking.views.addRoute),
    path('addRouteTrain/',booking.views.addRouteTrain),
]