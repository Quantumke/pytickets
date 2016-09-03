from django.contrib.auth.models import User
from django import forms
from app.models import *
class add_new_user(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username','email','password')

class loginuser(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username','password')
