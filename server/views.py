from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import ServerRegistrationForm

# Create your views here.

def home_server(request):
	context = {}
	return render(request, 'server/home_server.html', context)

def register_server(request):
	context = {}
	if request.POST:
		form = ServerRegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password')
			account = authenticate(email=email, password=raw_password)
			login(request, user)
			return redirect('core:home')
		else:
			context['server_registration_form'] = form
	else:
		form = ServerRegistrationForm()
		context['server_registration_form'] = form

	return render(request, 'server/register_server.html', context)