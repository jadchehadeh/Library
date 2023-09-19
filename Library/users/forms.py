from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserRegisterForm(UserCreationForm): #this form is used just to add a new fields to the generic form provided by django for Registration#
	email=forms.EmailField()

	class Meta:
		model=User
		fields=['username','email','password1','password2']
