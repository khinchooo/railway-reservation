from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from .forms import UserLogin, UserRegister
from django.contrib.auth import authenticate,login
from booking.models import Member

# Create your views here.
def Login(request):
    template = loader.get_template('booking/login.html')
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            user = authenticate(username = username, password = password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home/', request)
            return HttpResponse('Invalid username or password')
        return HttpResponse('Not Complete Data')
    else:
        return HttpResponse(template.render({}, request))

def Register(request):
    template = loader.get_template('booking/register.html')
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            data = form.cleaned_data
            username = data['username']
            password = data['password']
            email = data['email']
            number = data['number']
            member = Member()
            member.username = username
            member.password = password
            member.email = email
            member.number = number
            member.save()
            user.set_password(password)
            user.save()
            user= authenticate(username = username, password = password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request,'booking/home.html')
            return HttpResponse('valid')
        return HttpResponse(template.render({'form':form},request))
    else:
        return HttpResponse(template.render({}, request))

def home(request):
    return render(request,'booking/home.html')