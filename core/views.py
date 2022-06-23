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
	venues = [venue.venue_name for venue in Venue.objects.all() if str(venue.owner) == str(request.user.email)]
	if request.user != 'AnonymousUser':
		customer = [cust.location for cust in CustomerLocation.objects.all() if str(cust.customer) == str(request.user.email)]
	if customer:
		context = {'user':user, 'venues':venues, 'venue':venue, 'customer':customer[0]}
	else:
		context = {'user':user, 'venues':venues, 'venue':venue}
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
			return redirect('core:venue_page')
	
	context = {'user':user, 'form':form}
	return render(request, 'core/customer_location.html', context)

# Customer View of the venue's page
def venue_page(request):
	user = Account.objects.get(id=request.user.id)
	if request.user != 'AnonymousUser':
		customer = [cust for cust in CustomerLocation.objects.all() if str(cust.customer) == str(request.user.email)]
	customer_location = customer[0].location
	context = {'customer':customer, 'customer_location':customer_location}
	return render(request, 'core/venue_page.html', context)








