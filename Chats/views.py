from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, BlogUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import regForm, SendMessage




@login_required
def send(request):

	if request.method == 'POST' : 

		form = SendMessage(request.POST)
		if form.is_valid():
			message = form.save(commit = False)
			person = request.user
			message.sender = person.username
			message.save()
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
	return render(request, 'Blogs/register.html')