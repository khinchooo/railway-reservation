from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def Login(request):
    template = loader.get_template('booking/login.html')
    return HttpResponse(template.render({}, request))

def Register(request):
    template = loader.get_template('booking/register.html')
    return HttpResponse(template.render({}, request))