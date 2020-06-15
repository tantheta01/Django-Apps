from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import regForm, SendMessage
import time




@login_required
def send(request):

	if request.method == 'POST' : 

		form = SendMessage(request.POST)
		if form.is_valid():
			Message = form.save(commit = False)
			person = request.user
			Message.time_of_send = time.time()
			Message.sender = person.username
			Message.save()
			return redirect('somepage')
		else:
			form = SendMessage()

	else:
		form = SendMessage()
		return render(request, 'Chats/send.html', {'form' : form})

		


# Create your views here.


def regUser(request):

	if request.method == 'POST':
		form = regForm(request.POST)
		if form.is_valid():
			person = form.save()
			person.save()
			A = AppUser(user = person)
			A.save()
			return redirect('somewhere')

	else:
		form = regForm()
	return render(request, 'Chats/register.html', {'form' : form})



def login_user(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		person = authenticate(username = username, password = password)
		if person is not None:
			print("hola")
			login(request, person)
			return redirect('send')

		else:
			print("BBSDK")
	return render(request, 'Chats/login.html')

@login_required
def logout_user(request):
	logout(request)
	return redirect('regser')



@login_required
def query_message(request):

	person = request.user
	QSet = Message.filter(sender = person.username)
	