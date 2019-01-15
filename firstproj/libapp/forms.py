from django import forms
from libapp.models import User

class LoginForm(forms.Form):
  username = forms.CharField(max_length=10, label='',\
   widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}),
   error_messages={'required': 'Please enter the username'})
  password = forms.CharField(max_length=15, label='',\
   widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
   error_messages={'required': 'Please enter the password'})

class RegisterForm(forms.Form):
  username = forms.CharField(max_length=10, label='',\
   widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}),
   error_messages={'required': 'Please enter the username'})

  password = forms.CharField(max_length=15, label='',\
   widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
   error_messages={'required': 'Please enter the password'})

  country = forms.ChoiceField(choices=(('IN', 'India'),('NE', 'Netherlands')))
  gender = forms.ChoiceField(widget=forms.RadioSelect, choices=(('M', 'Male'),('F', 'Female')))

class RegisterModelForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username','password','gender','country']
    widgets = {
      'username': forms.TextInput(attrs={'placeholder': 'Enter Username'}),
      'password': forms.PasswordInput(attrs={'placeholder': 'Enter Password'})
    }
    labels = {
      'username': '',
      'password': ''
    }