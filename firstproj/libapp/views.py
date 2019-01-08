from django.shortcuts import render, reverse
from datetime import datetime
from django.http import HttpResponseRedirect
from libapp.models import User

# Create your views here.

def getgreeting():
  now = datetime.now()
  hour = now.hour
  if hour >= 0 and hour < 12:
    message = 'Good Morning'
  elif hour >= 12 and hour < 16:
    message = 'Good Afternoon'
  else:
    message = 'Good Evening'
  
  return message

def getcountries():
  # imagine u have got the countries from the database
  return [
    ('IN', 'India'),
    ('NE', 'Netherlands'),
    ('US', 'United states of america'),
    ('FR', 'France')
  ]

def showlogin(request):
  greeting = getgreeting()
  contextdata = {
    'greetingmsg': greeting
  }
  return render(request, 'libapp/login.html', contextdata)

def showregister(request):
  countries = getcountries()
  contextdata = {
    'countries': countries
  }
  return render(request, 'libapp/register.html', contextdata)

def createuser(request):
  postdata = request.POST
  username = postdata['username']
  password = postdata['password']
  country = postdata['country']
  gender = postdata['gender']

  u = User(username=username, password=password, gender=gender, country=country)
  u.save()


  return HttpResponseRedirect(reverse('login'))