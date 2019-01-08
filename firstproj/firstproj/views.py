from django.http import HttpResponse
from django.shortcuts import render

def hi(request):
  # return HttpResponse('<html><body><b>Hello World</b></body></html>')
  return render(request, 'hello.html')