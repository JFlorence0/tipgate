from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from core.models import ServerLocation
from users.models import Account

class ServerRegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=60, help_text="Enter valid email address.")
	class Meta:
		model = Account
		fields = ("email", "username", "first_name", "last_name", "is_server", "password1", "password2")

class AuthenticateServerForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	
	class Meta:
		model = Account
		fields = ('email', 'password')

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")

class ServerLocationForm(forms.ModelForm):

	class Meta:
		model = ServerLocation
		fields = ('location',)