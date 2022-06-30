from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import ServerRegistrationForm, AuthenticateServerForm, ServerLocationForm

from core.models import ServerLocation
from users.models import Account

# Create your views here.

def home_server(request):
	user = request.user
	context = {}
	# If user is not logged in
	if str(request.user) == 'AnonymousUser':
		context = {'user':user}
	else:
		user = Account.objects.get(id=request.user.id)
		if user.is_server == True:

			server_location = [server for server in ServerLocation.objects.all() if str(server.server) == str(request.user.email)]
			if len(server_location) > 0:
				server_location = server_location[0]
				context = {'server_location':server_location, 'user':user}
	
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
			return redirect('server:server_location')
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

def server_location(request, user_id):
	user = Account.objects.get(id=user_id)

	if user != request.user:
		raise Http404

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = ServerLocationForm()
	else:
		# POST data submitted; process data.
		form = ServerLocationForm(data=request.POST)
		if form.is_valid():
			server_location = form.save(commit=False)
			server_location.server = user
			server_location.save()
			return redirect('server:home_server')

	context = {'user':user, 'form':form}
	return render(request, 'server/server_location.html', context)

def server_dashboard(request, user_id):
	user = Account.objects.get(id=user_id)
	context = {'user':user}
	return render(request, 'server/server_dashboard.html', context)


def logged_out(request):
	logout(request)
	return render(request, 'server/logged_out.html')











