from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', hello1, name='hello'),
    path('',newhomepage,name = 'newhomepage'),
    path('travelpackage/',travelpackage,name = 'travelpackage'),
    path('anusha/',print_to_console,name='print_to_console'),
    path('print1',print1,name='print1'),
    path('randomlogic/',randomlogic,name='randomlogic'),
    path('randomcall',randomcall,name='randomcall'),
    path('getdate1',getdate1,name='getdate1'),
    path('get_date',get_date,name='get_date'),
    path('registercallfunction/',registercallfunction,name='registercallfunction'),
    path('registerloginfunction/',registerloginfunction,name='registerloginfunction'),
    path('pie_chart_call/',pie_chart_call,name='pie_chart_call'),
    path('pie_chart/',pie_chart,name='pie_chart'),
    path('cart_call/',cart_call,name='cart_call'),
    path('weathercall/',weathercall,name='weathercall'),
    path('weatherlogic/',weatherlogic,name='weatherlogic'),
    path('contactcall/', contactcall,name='contactcall'),
    path('contactmail/',contactmail,name='contactmail'),
    path('login/', login, name='login'),
    path('login1', login1, name='login1'),
    path('signup/', signup, name='signup'),
    path('signup1', signup1, name='signup1'),
    path('logout/', logout, name='logout'),
]