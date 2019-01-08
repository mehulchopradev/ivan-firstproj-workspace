from django.urls import path
from libapp.views import showlogin, showregister, createuser

# lib/

urlpatterns = [
  path('login/', showlogin, name='login'),
  path('register/', showregister, name='reg'),
  path('create-users/', createuser, name='createuser')
]
