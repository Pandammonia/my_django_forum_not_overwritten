from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
	"""Register page"""
	if request.method != 'POST':
		form = UserCreationForm()
	else:
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			#Log user in and return to page
			login(request, new_user)
			return redirect('myblog:home')

	#Display blank or invalid form
	context = {'form': form}
	return render(request, 'registration/register.html, context')
# Create your models here.
