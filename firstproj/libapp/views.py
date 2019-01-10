from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse
from libapp.models import User, Book
from libapp.service import getgreeting, getcountries

# Create your views here.

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

  if u.id:
    return HttpResponseRedirect(reverse('login'))
  else:
    return HttpResponse('Error in registration')

def authenticate(request):
  username, password = request.POST['username'], request.POST['password']
  l = User.objects.filter(username=username, password=password)
  if l:
    user = l[0]
    userid = user.id
    return HttpResponseRedirect(reverse('home'))
  else:
    return HttpResponseRedirect(reverse('login'))

def showhome(request):
  booklist = Book.objects.order_by('-price')
  contextdata = {
    'booklist': booklist
  }
  return render(request, 'libapp/home.html', contextdata)

def showbookdetails(request, bookid):
  # get the id (pk) of the book whose details we want ???
  # get the details of a particular book from the database
  book = Book.objects.get(pk=bookid)
  contextdata = {
    'book': book
  }
  return render(request, 'libapp/bookdetails.html', contextdata)