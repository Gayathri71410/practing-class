from django.shortcuts import render, redirect
from django.http import HttpResponse
import random
import string


from .forms import *
import matplotlib.pyplot as plt
import numpy as np

from .models import *
from django.shortcuts import render
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

def hello1(request):
    return HttpResponse("<center> Welcome to TTM HomePage </center>")

def newhomepage(request):
    return render(request,'newhomepage.html')

def travelpackage(request):
    return render(request,'travelpackage.html')

def print1(request):
    return render(request,'print_to_console.html')

def print_to_console(request):
    if request.method=="POST":
        anusha=request.POST['anusha']
        print(f"User input :{anusha}")
    a1={'anusha':anusha}
    return render(request,'print_to_console.html',a1)

def randomcall(request):
    return render(request,'randomOTPGenerator.html')

def randomlogic(request):
    if request.method=="POST":
        anusha=request.POST['anusha']
        print(f"User input :{anusha}")
        a2 = int(anusha)
        ran1 = ' '.join(random.sample(string.digits, k=a2))
    a1={'ran1':ran1}
    return render(request,'randomOTPGenerator.html',a1)

def getdate1(request):
    return render(request,'date1.html')

import datetime
from django.shortcuts import render
def get_date(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value=form.cleaned_data['integer_value']
            date_value=form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request,'date1.html',{'updated_date': updated_date})
        else:
            form=IntegerDateForm()
        return render(request,'date1.html',{'form':form})


def registercallfunction(request):
    return render(request, 'myregister.html')
from .models import *
from django.shortcuts import render,redirect
def registerloginfunction(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')

        if Register.objects.filter(email=email).exists():
            return HttpResponse("Email already registered choose a different email.")
        Register.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('newhomepage.html')
    return render(request,'myregister.html')

def pie_chart_call(request):
    return render(request,'graphs.html')

def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'graphs.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'graphs.html', {'form': form})

def cart_call(request):
    return render(request,'cart.html')


import requests
def weathercall(request):
    return render(request,'weatherapp.html')


def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '09ef3e51db198873e695df6da38b9bd0'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherapp.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherapp.html', {'error_message': error_message})

from django.core.mail import send_mail
from django.shortcuts import render,redirect
from.models import *
def contactmail(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        tosend = comment + '.........this is just the copy .........'
        data=contactus(firstname=firstname, lastname=lastname, email=email, comment=comment)
        data.save()
        # return Httpresponse ("<h1><center> thank you for giving your feedback
        send_mail(
            ' thank you contacting Lavenias travel tourism and management',
            tosend,
            '2200010045cseh@gmail.com',   # change this to your id...
            [email],
            fail_silently=False,
        )
        return HttpResponse("<h1><center>Mail sent</center></h1>")
    else:
        HttpResponse("<h1>error</h1>")
        # return redirect('newhomepage')
        # return render(request,'contact.html')

        return HttpResponse("Sucess")


def contactcall(request):
    return render(request,'feedback.html')

def login(request) :
    return render(request, 'login.html')

def signup(request):
    return render(request,'signup.html')


def login1(request):
    if request.method == 'POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None :
            auth.login(request,user)
            return render(request,'newhomepage.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def signup1(request):
 if request.method=="POST":
    username=request.POST['username']
    pass1=request.POST['password']
    pass2=request.POST['password1']
    if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Usename already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!!')
                return render(request,'login.html')
    else:
            messages.info(request,'Password do not match')
            return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return render (request,'newhomepage.html')