from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.views import View
from django.views.generic.edit import FormView
from libapp.models import User, Book
from libapp.service import getgreeting, getcountries
from libapp.forms import LoginForm, RegisterForm

# Create your views here.

class RegisterFormView(FormView):
  template_name = 'libapp/register.html'
  form_class = RegisterForm

  def form_valid(self, form):
    data = form.cleaned_data

    u = User(**data)
    u.save()

    if u.id:
      return HttpResponseRedirect(reverse('login'))
    else:
      return render(request, 'libapp/register.html', {
        'form': form,
      })

class RegisterView(View):
  def get(self, request):
    form = RegisterForm()

    return render(request, 'libapp/register.html', {
      'form': form,
    })

  def post(self, request):
    form = RegisterForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data

      u = User(**data)
      u.save()

      if u.id:
        return HttpResponseRedirect(reverse('login'))
    
    return render(request, 'libapp/register.html', {
      'form': form,
    })

class AuthView(View):
  def get(self, request):
    greeting = getgreeting()
    form = LoginForm()

    return render(request, 'libapp/login.html', {
      'form': form,
      'greetingmsg': greeting
    })

  def post(self, request):
    greeting = getgreeting()

    form = LoginForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      username, password = data['username'], data['password']

      l = User.objects.filter(username=data['username'], password=data['password'])
      if l:
        user = l[0]
        userid = user.id
        session = request.session
        session['username'] = username
        session['userid'] = userid

        return HttpResponseRedirect(reverse('home'))
    
    return render(request, 'libapp/login.html', {
      'form': form,
      'greetingmsg': greeting
    })

'''def authform(request):
  greeting = getgreeting()

  # GET
  if request.method == 'GET':
    form = LoginForm()
  else:
    form = LoginForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      username, password = data['username'], data['password']

      l = User.objects.filter(username=data['username'], password=data['password'])
      if l:
        user = l[0]
        userid = user.id
        session = request.session
        session['username'] = username
        session['userid'] = userid

        return HttpResponseRedirect(reverse('home'))
  
  return render(request, 'libapp/login.html', {
    'form': form,
    'greetingmsg': greeting
  })'''

def showlogin(request):
  greeting = getgreeting()
  contextdata = {
    'greetingmsg': greeting,
    'form': LoginForm()
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
    session = request.session
    session['username'] = username
    session['userid'] = userid

    return HttpResponseRedirect(reverse('home'))
  else:
    return HttpResponseRedirect(reverse('login'))

def showhome(request):
  session = request.session
  if 'username' not in session:
    return HttpResponseRedirect(reverse('login'))

  userid = request.session['userid']
  booklist = Book.objects.order_by('-price')
  for book in booklist:
    if book.user_set.filter(pk=userid):
      book.alreadyissued = True
    else:
      if book.quantity - book.user_set.count():
        book.canbeissued = True
      else:
        book.canbeissued = False

  contextdata = {
    'booklist': booklist,
    'username': session['username']
  }
  return render(request, 'libapp/home.html', contextdata)

def showbookdetails(request, bookid):
  # get the id (pk) of the book whose details we want ???
  # get the details of a particular book from the database
  session = request.session
  if 'username' not in session:
    return HttpResponseRedirect(reverse('login'))

  book = Book.objects.get(pk=bookid)
  contextdata = {
    'book': book,
    'username': session['username']
  }
  return render(request, 'libapp/bookdetails.html', contextdata)

def logout(request):
  session = request.session
  session.flush()

  return HttpResponseRedirect(reverse('login'))

def issuebook(request, bookid):
  book = Book.objects.get(pk=bookid)
  userid = request.session['userid']
  user = User.objects.get(pk=userid)

  user.booksissued.add(book)

  return HttpResponseRedirect(reverse('home'))

def returnbook(request, bookid):
  user = User.objects.get(pk=request.session['userid'])
  user.booksissued.remove(bookid)

  return HttpResponseRedirect(reverse('home'))