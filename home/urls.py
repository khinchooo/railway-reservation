from django.contrib import admin
from django.urls import path
import booking
from . import views
app_name='home'
urlpatterns = [
    path('',views.Home,name="hom" ),
    path('logout/',views.logout),
    path('search/',booking.views.search),
    path('search/trains',booking.views.getTrain),
    # path('search/search/trains/cva/', booking.views.cva),
    # path('search/book1/', booking.views.book1),
    #  path('cancel/',booking.views.cancel),
]