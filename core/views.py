from django.shortcuts import render, redirect

# Create your views here.
def home(request):
	""" Display the home page """
	return render(request, 'core/home.html')