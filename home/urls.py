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
]