from django.urls import path
from libapp.views import showlogin, showregister

# lib/

urlpatterns = [
  path('login/', showlogin),
  path('register/', showregister, name='reg')
]
