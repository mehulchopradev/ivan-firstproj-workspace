from django.urls import path
from libapp.views import showlogin, showregister, createuser, authenticate, showhome, showbookdetails

# lib/

# path params (data is part of the regular url format)
# lib/book-details/1
# lib/book-details/4

urlpatterns = [
  path('login/', showlogin, name='login'),
  path('register/', showregister, name='reg'),
  path('create-users/', createuser, name='createuser'),
  path('auth/', authenticate, name='auth'),
  path('home/', showhome, name='home'),
  path('book-details/<int:bookid>', showbookdetails, name='bookdetails')
]
