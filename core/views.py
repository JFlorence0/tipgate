from django.shortcuts import render, redirect
from users.models import Account

from .models import (
	Venue, CustomerLocation, Menu, SideDish, Drink, 
	MainCourse, MainCourseVideo, SideDishVideo, DrinkVideo,
	CustomMenu, CustomEntree, CustomSideDish, CustomDrink,
	CustomEntreeVideo, CustomSideDishVideo, CustomDrinkVideo, SelectCustomMenu)

from .forms import VenueForm, CustomerLocationForm, MenuForm, MainCourseForm, MainCourseVideoForm
from .forms import SideDishForm, SideDishVideoForm, DrinkForm, DrinkVideoForm
from .forms import CustomMenuForm, CustomEntreeForm, CustomSideDishForm, CustomDrinkForm
from .forms import CustomEntreeVideoForm, CustomSideDishVideoForm, CustomDrinkVideoForm, SelectCustomMenuForm

# Create your views here.
def home(request):
	return render(request, 'core/home.html')

def manage_menus(request, user_id):
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
	return render(request, 'core/manage_menus.html', context)


def venue_form(request, user_id):
	user = Account.objects.get(id=user_id)

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

def edit_menu(request, user_id):
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
			if str(item.side_dish_item) == str(side):
				has_video.append(side)
				break
	for item in DrinkVideo.objects.all():
		for drink in Drink.objects.all():
			if str(item.drink_item) == str(drink):
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
		'sides':sides, 'drinks':drinks}
	return render(request, 'core/edit_menu.html', context)

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
			return redirect('core:edit_menu', user_id)
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
			return redirect('core:edit_menu', user_id=request.user.id)

	context = {'entree':entree, 'form':form}
	return render(request, 'core/edit_main_course.html', context)

	
def remove_main_course(request, entree_id):
	entree = MainCourse.objects.get(id=entree_id)
	entree.delete()
	return render(request, 'core/edit_menu.html')

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
	side = SideDish.objects.get(id=side_id)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current values
		form = SideDishForm(instance=side)
	else:
		# POST data submitted; process data.
		form = SideDishForm(instance=side, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('core:edit_menu', user_id=request.user.id)

	context = {'side':side, 'form':form}
	return render(request, 'core/edit_side_dish.html', context)
	

# Add a video for a side dish
def add_side_dish_video(request, side_id):
	side = SideDish.objects.get(id=side_id)
	video = [item.video for item in SideDishVideo.objects.all() if str(item.side_dish_item.name) == str(side)]
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
	video = [item.video for item in DrinkVideo.objects.all() if str(item.drink_item.name) == str(drink)]
	if video:
		video = video[-1]
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = DrinkVideoForm()
	else:
		# POST data submitted; process data.
		form = DrinkVideoForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('core:entree_view', drink_id=drink.id)
	context = {'drink':drink, 'video':video, 'form':form}
	return render(request, 'core/add_drink_video.html', context)


def edit_drink(request, drink_id):
	drink = Drink.objects.get(id=drink_id)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current values
		form = DrinkForm(instance=drink)
	else:
		# POST data submitted; process data.
		form = DrinkForm(instance=drink, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('core:edit_menu', user_id=request.user.id)

	context = {'drink':drink, 'form':form}
	return render(request, 'core/edit_drink.html', context)


def create_custom_menu(request, user_id):
	user = Account.objects.get(id=user_id)
	venue_instance = [venue for venue in Venue.objects.all() if str(venue.owner) == str(request.user.email)]
	if venue_instance:
		venue_instance = venue_instance[0]
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = CustomMenuForm()
	else:
		# POST data submitted; process data.
		form = CustomMenuForm(data=request.POST)
		if form.is_valid():
			venue_custom_menu = form.save(commit=False)
			venue_custom_menu.owner = venue_instance
			venue_custom_menu.save()
			return redirect('core:create_custom_menu', user_id)
	context = {'user':user, 'form':form}
	return render(request, 'core/create_custom_menu.html', context)

def select_custom_menu(request, user_id):
	user = Account.objects.get(id=user_id)
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = SelectCustomMenuForm()
	else:
		# POST data submitted; process data.
		form = SelectCustomMenuForm(data=request.POST)
		if form.is_valid():
			menu_selection = form.save(commit=False)
			menu_selection.owner = user
			menu_selection.save()
			return redirect('core:edit_custom_menu', user_id)
	context = {'user':user, 'form':form}
	return render(request, 'core/select_custom_menu.html', context)


def edit_custom_menu(request, user_id):
	user = Account.objects.get(id=user_id)
	selected_venue = [menu.venue for menu in SelectCustomMenu.objects.all() if str(menu.owner) == str(request.user.email)]
	if selected_venue:
		selected_venue = selected_venue[-1]
	print(selected_venue)
	menu = [menu for menu in CustomMenu.objects.all() if str(menu.custom_menu_owner.venue_name) == str(selected_venue)]
	if menu:
		menu = menu[-1]
	entrees = [entree for entree in CustomEntree.objects.all() if str(entree.custom_menu.custom_menu_owner.venue_name) == str(selected_venue)]
	sides = [side for side in CustomSideDish.objects.all() if str(side.custom_menu.custom_menu_owner.venue_name) == str(selected_venue)]
	drinks = [drink for drink in CustomDrink.objects.all() if str(drink.custom_menu.custom_menu_owner.venue_name) == str(selected_venue)]
	print(drinks)
	context = {'user':user, 'entrees':entrees, 'sides':sides, 'drinks':drinks}
	return render(request, 'core/edit_custom_menu.html', context)

def view_custom_menu(request, user_id):
	user = Account.objects.get(id=user_id)
	context = {'user':user}
	return render(request, 'core/view_custom_menu.html', context)


def add_custom_entree(request, user_id):
	user = Account.objects.get(id=user_id)
	custom_menu_instance = [menu for menu in CustomMenu.objects.all() if str(menu.custom_menu_owner.owner) == str(request.user.email)]
	if custom_menu_instance:
		custom_menu_instance = custom_menu_instance[-1]

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = CustomEntreeForm()
	else:
		# POST data submitted; process data.
		form = CustomEntreeForm(data=request.POST)
		if form.is_valid():
			entree = form.save(commit=False)
			entree.custom_menu = custom_menu_instance
			entree.save()
			return redirect('core:add_custom_entree', user_id=user.id)
	context = {'user':user, 'form':form}
	return render(request, 'core/add_custom_entree.html', context)

def edit_custom_entree(request, entree_id):
	entree = CustomEntree.objects.get(id=entree_id)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current values
		form = CustomEntreeForm(instance=entree)
	else:
		# POST data submitted; process data.
		form = CustomEntreeForm(instance=entree, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('core:edit_custom_menu', user_id=request.user.id)

	context = {'entree':entree, 'form':form}
	return render(request, 'core/edit_custom_entree.html', context)


# Add a video for the custom entree
def add_custom_entree_video(request, entree_id):
	custom_entree = CustomEntree.objects.get(id=entree_id)
	video = [item.video for item in CustomEntreeVideo.objects.all() if str(item.custom_entree.name) == str(custom_entree)]
	if video:
		video = video[-1]
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = CustomEntreeVideoForm()
	else:
		# POST data submitted; process data.
		form = CustomEntreeVideoForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('core:home')
	context = {'custom_entree':custom_entree, 'form':form, 'video':video}
	return render(request, 'core/add_custom_entree_video.html', context)


def add_custom_side(request, user_id):
	user = Account.objects.get(id=user_id)
	custom_menu_instance = [menu for menu in CustomMenu.objects.all() if str(menu.custom_menu_owner.owner) == str(request.user.email)]
	custom_menu_instance = custom_menu_instance[-1]

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = CustomSideDishForm()
	else:
		# POST data submitted; process data.
		form = CustomSideDishForm(data=request.POST)
		if form.is_valid():
			side_dish = form.save(commit=False)
			side_dish.custom_menu = custom_menu_instance
			side_dish.save()
			return redirect('core:add_custom_side', user_id=user.id)
	context = {'user':user, 'form':form}
	return render(request, 'core/add_custom_side.html', context)

def edit_custom_side(request, side_id):
	side = CustomSideDish.objects.get(id=side_id)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current values
		form = CustomSideDishForm(instance=side)
	else:
		# POST data submitted; process data.
		form = CustomSideDishForm(instance=side, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('core:edit_custom_menu', user_id=request.user.id)

	context = {'side':side, 'form':form}
	return render(request, 'core/edit_custom_side.html', context)

# Add a video for the custom side
def add_custom_side_video(request, side_id):
	custom_side = CustomSideDish.objects.get(id=side_id)
	video = [item.video for item in CustomSideDishVideo.objects.all() if str(item.custom_side_dish.name) == str(custom_side)]
	if video:
		video = video[-1]
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = CustomSideDishVideoForm()
	else:
		# POST data submitted; process data.
		form = CustomSideDishVideoForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('core:home')
	context = {'custom_side':custom_side, 'form':form, 'video':video}
	return render(request, 'core/add_custom_side_video.html', context)


def add_custom_drink(request, user_id):
	user = Account.objects.get(id=user_id)
	custom_menu_instance = [menu for menu in CustomMenu.objects.all() if str(menu.custom_menu_owner.owner) == str(request.user.email)]
	custom_menu_instance = custom_menu_instance[-1]

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = CustomDrinkForm()
	else:
		# POST data submitted; process data.
		form = CustomDrinkForm(data=request.POST)
		if form.is_valid():
			drink = form.save(commit=False)
			drink.custom_menu = custom_menu_instance
			drink.save()
			return redirect('core:add_custom_drink', user_id=user.id)
	context = {'user':user, 'form':form}
	return render(request, 'core/add_custom_drink.html', context)

def edit_custom_drink(request, drink_id):
	drink = CustomDrink.objects.get(id=drink_id)

	if request.method != 'POST':
		# Initial request; pre-fill form with the current values
		form = CustomDrinkForm(instance=drink)
	else:
		# POST data submitted; process data.
		form = CustomDrinkForm(instance=drink, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('core:edit_menu', user_id=request.user.id)

	context = {'drink':drink, 'form':form}
	return render(request, 'core/edit_custom_drink.html', context)	


# Add a video for the custom side
def add_custom_drink_video(request, drink_id):
	custom_drink = CustomDrink.objects.get(id=drink_id)
	video = [item.video for item in CustomDrinkVideo.objects.all() if str(item.custom_drink.name) == str(custom_drink)]
	if video:
		video = video[-1]
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = CustomDrinkVideoForm()
	else:
		# POST data submitted; process data.
		form = CustomDrinkVideoForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			form.save()
			return redirect('core:home')
	context = {'custom_drink':custom_drink, 'form':form, 'video':video}
	return render(request, 'core/add_custom_drink_video.html', context)






