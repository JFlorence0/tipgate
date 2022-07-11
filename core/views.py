from django.shortcuts import render, redirect
from users.models import Account

from .models import Venue, CustomerLocation, Menu, MainCourse, MainCourseVideo
from .models import SideDish, SideDishVideo, Drink, DrinkVideo

from .forms import VenueForm, CustomerLocationForm, MenuForm, MainCourseForm, MainCourseVideoForm
from .forms import SideDishForm, SideDishVideoForm, DrinkForm, DrinkVideoForm
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
			num_venues = len(venues)
			context = {'user':user, 'venues':venues, 'num_venues':num_venues}
			# Check if venue has a menu
			menu = [menu for menu in Menu.objects.all() if str(menu.menu_owner) == str(request.user.email)]
			if len(menu) > 0:
				context = {'user':user, 'venues':venues, 'menu':menu}

		# User is a customer
		else:
			if user.is_server:
				return redirect('server:home_server')
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

# Update customer location if they already have one
def update_customer_location(request, user_id):
	user = Account.objects.get(id=user_id)
	customer_location = [cust for cust in CustomerLocation.objects.all() if str(cust.customer) == str(request.user.email)]
	customer_location = customer_location[0]

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = CustomerLocationForm(instance=customer_location)
	else:
		# POST data submitted; process data.
		form = CustomerLocationForm(instance=customer_location, data=request.POST)
		if form.is_valid():
			customer_location.save()
			return redirect('core:home')
	context = {'user':user,'form':form, 'customer_location':customer_location}
	return render(request, 'core/update_customer_location.html', context)


# Customer View of the venue's page
def venue_page(request, user_id):
	user = Account.objects.get(id=user_id)
	if request.user != 'AnonymousUser':
		customer = [cust for cust in CustomerLocation.objects.all() if str(cust.customer) == str(request.user.email)]
	customer_location = customer[0].location
	context = {'customer':customer, 'customer_location':customer_location}
	return render(request, 'core/venue_page.html', context)


# Venues enter their menu items
def create_base_menu(request, user_id):
	user = Account.objects.get(id=user_id)
	venue_instance = [venue for venue in Venue.objects.all() if str(venue.owner) == str(request.user.email)]
	if venue_instance:
		venue_instance = venue_instance[0]
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = MenuForm()
	else:
		# POST data submitted; process data.
		form = MenuForm(data=request.POST)
		if form.is_valid():
			venue_menu = form.save(commit=False)
			venue_menu.owner = user
			venue_menu.save()
			return redirect('core:venue_menu_view', user_id)
	context = {'user':user, 'form':form}
	return render(request, 'core/create_base_menu.html', context)

# Menu view from the venue's POV
def venue_menu_view(request, user_id):
	user = Account.objects.get(id=user_id)
	entrees = [entree for entree in MainCourse.objects.all() if str(entree.menu.menu_owner) == str(request.user.email)]
	sides = [side for side in SideDish.objects.all() if str(side.menu.menu_owner) == str(request.user.email)]
	has_video = []
	for item in MainCourseVideo.objects.all():
		for entree in MainCourse.objects.all():
			if str(item.main_course_item) == str(entree):
				has_video.append(entree)
				break
	for item in SideDishVideo.objects.all():
		for side in SideDish.objects.all():
			if str(item.main_course_item) == str(side):
				has_video.append(side)
				break
	no_video = []
	for entree in entrees:
		if entree not in has_video:
			no_video.append(entree)

	context = {'user':user, 'entrees':entrees, 'sides':sides, 'has_video':has_video, 'no_video':no_video}
	return render(request, 'core/venue_menu_view.html', context)

# Add main course to the base menu
def add_main_course(request, user_id):
	user = Account.objects.get(id=user_id)
	menu_instance = [menu for menu in Menu.objects.all() if str(menu.menu_owner) == str(request.user.email)]
	menu_instance = menu_instance[0]

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = MainCourseForm()
	else:
		# POST data submitted; process data.
		form = MainCourseForm(data=request.POST)
		if form.is_valid():
			main_course = form.save(commit=False)
			main_course.menu = menu_instance
			main_course.save()
			return redirect('core:home')
	context = {'user':user, 'form':form}
	return render(request, 'core/add_main_course.html', context)

def edit_main_course(request, entree_id):
	entree = MainCourse.objects.get(id=entree_id)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current values
		form = MainCourseForm(instance=entree)
	else:
		# POST data submitted; process data.
		form = MainCourseForm(instance=entree, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('core:video', user_id=request.user.id)

	context = {'entree':entree, 'form':form}
	return render(request, 'core/edit_main_course.html', context)

# Add a video for the main course
def add_main_course_video(request, entree_id):
	entree = MainCourse.objects.get(id=entree_id)
	video = [item.video for item in MainCourseVideo.objects.all() if str(item.main_course_item.name) == str(entree)]
	if video:
		video = video[-1]
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = MainCourseVideoForm()
	else:
		# POST data submitted; process data.
		form = MainCourseVideoForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('core:entree_view', entree_id=entree.id)
	context = {'entree':entree, 'form':form, 'video':video}
	return render(request, 'core/add_main_course_video.html', context)


def entree_view(request, entree_id):
	entree = MainCourse.objects.get(id=entree_id)
	video = [item.video for item in MainCourseVideo.objects.all() if str(item.main_course_item.name) == str(entree)]
	if video:
		video = video[-1]
	context = {'entree':entree, 'video':video}
	return render(request, 'core/entree_view.html', context)

# Add a side dish to the menu
def add_side_dish(request, user_id):
	user = Account.objects.get(id=user_id)
	menu_instance = [menu for menu in Menu.objects.all() if str(menu.menu_owner) == str(request.user.email)]
	menu_instance = menu_instance[0]

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = SideDishForm()
	else:
		# POST data submitted; process data.
		form = SideDishForm(data=request.POST)
		if form.is_valid():
			side_dish = form.save(commit=False)
			side_dish.menu = menu_instance
			side_dish.save()
			return redirect('core:add_side_dish', user_id)
	context = {'user':user, 'form':form}
	return render(request, 'core/add_side_dish.html', context)

def edit_side_dish(request, side_id):
	side = MainCourse.objects.get(id=side_id)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current values
		form = SideDishForm(instance=side)
	else:
		# POST data submitted; process data.
		form = SideDishForm(instance=side, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('core:video', user_id=request.user.id)

	context = {'entree':entree, 'form':form, 'side':side}
	return render(request, 'core/edit_main_course.html', context)

# Add a video for a side dish
def add_side_dish_video(request, side_id):
	side = SideDish.objects.get(id=side_id)
	video = [item.video for item in MainCourseVideo.objects.all() if str(item.main_course_item.name) == str(side)]
	if video:
		video = video[-1]
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = SideDishVideoForm()
	else:
		# POST data submitted; process data.
		form = SideDishVideoForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('core:entree_view', side_id=side.id)
	context = {'side':side, 'form':form, 'video':video}
	return render(request, 'core/add_side_dish_video.html', context)


def add_drink(request, user_id):
	user = Account.objects.get(id=user_id)
	menu_instance = [menu for menu in Menu.objects.all() if str(menu.menu_owner) == str(request.user.email)]
	menu_instance = menu_instance[0]

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = DrinkForm()
	else:
		# POST data submitted; process data.
		form = DrinkForm(data=request.POST)
		if form.is_valid():
			drink = form.save(commit=False)
			drink.menu = menu_instance
			drink.save()
			return redirect('core:add_drink', user_id)
	context = {'user':user, 'form':form}
	return render(request, 'core/add_drink.html', context)

# Add a video for a side dish
def add_drink_video(request, drink_id):
	drink = Drink.objects.get(id=drink_id)
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = DrinkVideoForm()
	else:
		# POST data submitted; process data.
		form = DrinkVideoForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('core:entree_view', drink_id=drink.id)
	context = {'drink':drink, 'form':form}
	return render(request, 'core/add_drink_video.html', context)

def video(request, user_id):
	entrees = [entree for entree in MainCourse.objects.all() if str(entree.menu.menu_owner) == str(request.user.email)]
	sides = [side for side in SideDish.objects.all() if str(side.menu.menu_owner) == str(request.user.email)]
	drinks = [drink for drink in Drink.objects.all() if str(drink.menu.menu_owner) == str(request.user.email)]
	has_video = []
	for item in MainCourseVideo.objects.all():
		for entree in MainCourse.objects.all():
			if str(item.main_course_item) == str(entree):
				has_video.append(entree)
				break
	for item in SideDishVideo.objects.all():
		for side in SideDish.objects.all():
			if str(item.main_course_item) == str(side):
				has_video.append(side)
				break
	for item in DrinkVideo.objects.all():
		for drink in Drink.objects.all():
			if str(item.main_course_item) == str(drink):
				has_video.append(drink)
				break
	no_video = []
	for entree in entrees:
		if entree not in has_video:
			no_video.append(entree)

	for side in sides:
		if side not in has_video:
			no_video.append(side)

	for drink in drinks:
		if drink not in has_video:
			no_video.append(drink)
	context = {'entrees':entrees, 'has_video':has_video, 'no_video':no_video,
		'sides':sides}
	return render(request, 'core/video.html', context)







