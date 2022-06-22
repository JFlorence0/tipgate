from django.shortcuts import render, redirect
from users.models import Account
from .models import Venue, CustomerLocation
from .forms import VenueForm, CustomerLocationForm

# Create your views here.
def home(request):
	""" Display the home page """
	user = request.user
	venue = Venue.objects.all()
	if venue:
		venue = venue[0]
	customer = CustomerLocation.objects.get(id=request.user.id)
	venues = [venue for venue in Account.objects.all() if venue.is_venue == True]
	context = {'user':user, 'venues':venues, 'venue':venue, 'customer':customer}
	return render(request, 'core/home.html', context)

def venue_form(request, user_id):
	user = Account.objects.get(id=user_id)

	if user != request.user:
		raise Http404

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = VenueForm()
	else:
		# POST data submitted; process data.
		form = VenueForm(data=request.POST)
		if form.is_valid():
			venue = form.save(commit=False)
			venue.owner = user
			venue.save()
			return redirect('core:home')
	

	context = {'user':user, 'form':form}
	return render(request, 'core/venue_form.html', context)
	
def customer_location(request, user_id):
	user = Account.objects.get(id=user_id)

	if user != request.user:
		raise Http404

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = CustomerLocationForm()
	else:
		# POST data submitted; process data.
		form = CustomerLocationForm(data=request.POST)
		if form.is_valid():
			customer_location = form.save(commit=False)
			customer_location.customer = user
			customer_location.save()
			return redirect('core:home')
	

	context = {'user':user, 'form':form}
	return render(request, 'core/customer_location.html', context)

