from django import forms
from .models import message, ChatUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class regForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name' 'password1', 'password2', 'email')


class SendMessage(forms.ModelForm):

	class Meta:
		model = message
		fields = ('messageText', 'sender', 'receiver')

		