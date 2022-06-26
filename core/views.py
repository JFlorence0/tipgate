from django.shortcuts import render, redirect
from users.models import Account
from .models import Venue, CustomerLocation, Menu

from .forms import VenueForm, CustomerLocationForm, MenuForm

# Create your views here.
def home(request):
	""" Display the home page """
	user = request.user

	# User is not logged in
	if str(request.user) == 'AnonymousUser':
		context = {'user':user}
	# User is logged in
	else:
		# User is a venue
		if request.user.is_venue == True:
			venues = [venue for venue in Venue.objects.all() if str(venue.owner) == str(request.user.email)]
			context = {'user':user, 'venues':venues}
			# Check if venue has a menu
			menu = [print(menu.menu_owner.venue_name) for menu in Menu.objects.all() if str(menu.menu_owner.owner) == str(request.user.email)]
			if len(menu) > 0:
				context = {'user':user, 'venues':venues, 'menu':menu}

		# User is a customer
		else:
			customer_location = [cust.location for cust in CustomerLocation.objects.all() if str(cust.customer) == str(request.user.email)]
			# Check if the user has entered a location
			if len(customer_location) > 0:
				context = {'user':user, 'customer_location':customer_location[0]}
			else:
				context = {'user':user}
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
			return redirect('core:venue_page', user_id)
	
	context = {'user':user, 'form':form}
	return render(request, 'core/customer_location.html', context)


# Customer View of the venue's page
def venue_page(request, user_id):
	user = Account.objects.get(id=user_id)
	if request.user != 'AnonymousUser':
		customer = [cust for cust in CustomerLocation.objects.all() if str(cust.customer) == str(request.user.email)]
	customer_location = customer[0].location
	context = {'customer':customer, 'customer_location':customer_location}
	return render(request, 'core/venue_page.html', context)


# Venues enter their menu items
def build_menu(request, user_id):
	user = Account.objects.get(id=user_id)
	venue_instance = [venue for venue in Venue.objects.all() if str(venue.owner) == str(request.user.email)]
	venue_instance = venue_instance[0]
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = MenuForm()
	else:
		# POST data submitted; process data.
		form = MenuForm(data=request.POST)
		if form.is_valid():
			venue_menu = form.save(commit=False)
			venue_menu.owner = venue_instance
			venue_menu.save()
			return redirect('core:menu_items', user_id)
	context = {'user':user, 'venue_instance':venue_instance, 'form':form}
	return render(request, 'core/build_menu.html', context)

def menu_items(request, user_id):
	user = Account.objects.get(user_id)
	context = {'user':user}
	return render(request, 'core/menu_items.html')








