from django.shortcuts import render

# Create your views here.

def showlogin(request):
  return render(request, 'libapp/login.html')

def showregister(request):
  return render(request, 'libapp/register.html')
