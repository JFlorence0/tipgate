from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegistrationForm, AuthenticateUserForm



# Create your views here.
def register(request):
	context = {}
	if request.POST:
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			email = form.cleaned_data.get('email')
			raw_password = form.cleaned_data.get('password')
			account = authenticate(email=email, password=raw_password)
			login(request, user)
			return redirect('core:home')
		else:
			context['registration_form'] = form
	else:
		form = RegistrationForm()
		context['registration_form'] = form

	return render(request, 'registration/register.html', context)

def authenticate_user(request):
	context= {}
	user = request.user
	if user.is_authenticated:
		return redirect('core:home')

	if request.POST:
		form = AuthenticateUserForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(email=email, password=password)

			if user:
				login(request, user)
				return redirect('core:home')
	else:
		form = AuthenticateUserForm()

	context['authenticate_form'] = form
	return render(request, 'registration/authenticate_user.html', context)

def logged_out(request):
	logout(request)
	return render(request, 'users/logged_out.html')

