from django.shortcuts import render

# Create your views here.

def home_server(request):
	context = {}
	return render(request, 'server/home_server.html', context)