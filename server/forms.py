from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from users.models import Account

class ServerRegistrationForm(UserCreationForm):
	email = forms.EmailField(max_length=60, help_text="Enter valid email address.")
	class Meta:
		model = Account
		fields = ("email", "username", "first_name", "last_name", "is_venue", "password1", "password2")