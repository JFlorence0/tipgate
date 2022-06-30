from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import ServerRegistrationForm, AuthenticateServerForm

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
			return redirect('server:home_server')
		else:
			context['server_registration_form'] = form
	else:
		form = ServerRegistrationForm()
		context['server_registration_form'] = form

	return render(request, 'server/register_server.html', context)

def authenticate_server(request):
	context= {}
	user = request.user
	if user.is_authenticated:
		return redirect('server:home_server')

	if request.POST:
		form = AuthenticateServerForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect('server:home_server')
	else:
		form = AuthenticateServerForm()

	context['authenticate_server_form'] = form
	return render(request, 'server/authenticate_server.html', context)

def logged_out(request):
	logout(request)
	return render(request, 'server/logged_out.html')











