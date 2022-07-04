from django.shortcuts import render, redirect

from users.models import Account
from core.models import CustomerLocation, CustomerOrder, MainCourse, Venue
from core.models import MainCourseIngredient, SideDishIngredient, DrinkIngredient

from .forms import CustomerOrderForm

# Create your views here.
def place_order(request, user_id):
	user = Account.objects.get(id=user_id)
	customer_location = [cust.location for cust in CustomerLocation.objects.all() if str(cust.customer) == str(request.user.email)]
	customer_location = customer_location[0]

	if user != request.user:
		raise Http404

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = CustomerOrderForm()
	else:
		# POST data submitted; process data.
		form = CustomerOrderForm(data=request.POST)
		if form.is_valid():
			customer_order = form.save(commit=False)
			customer_order.customer = user
			customer_order.save()
			return redirect('orders:edit_ingredients', user_id)

	context = {'user':user, 'customer_location':customer_location, 'form':form}
	return render(request, 'orders/place_order.html', context)

def edit_ingredients(request, user_id):
	user = Account.objects.get(id=user_id)
	customer_location = [cust.location for cust in CustomerLocation.objects.all() if str(cust.customer) == str(request.user.email)]
	customer_location = customer_location[0]
	venue = [venue for venue in Venue.objects.all() if str(venue.venue_name) == str(customer_location)]
	venue = venue[0]
	entree = [order_item.entree for order_item in CustomerOrder.objects.all() if str(order_item.customer) == str(request.user.email)]
	if len(entree) == 1:
		entree = entree[0]
	side = [order_item.side for order_item in CustomerOrder.objects.all() if str(order_item.customer) == str(request.user.email)]
	side = side[0]
	drink = [order_item.drink for order_item in CustomerOrder.objects.all() if str(order_item.customer) == str(request.user.email)]
	drink = drink[0]
	order_id = [order_item.id for order_item in CustomerOrder.objects.all() if str(order_item.customer) == str(request.user.email)]

	main_course_ingredient = [print(item_ingrdient) for item_ingredient in MainCourseIngredient.objects.all() if str(item_ingredient.item.name) == str(entree)]
	context = {'user':user, 'entree':entree, 'side':side,
		'drink':drink, 'order_id':order_id, 'main_course_ingredient':main_course_ingredient}
	return render(request, 'orders/edit_ingredients.html', context)

def edit_entree(request, user_id):
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = CustomerLocationForm(instance=customer_location)
	else:
		# POST data submitted; process data.
		form = CustomerLocationForm(instance=customer_location, data=request.POST)
		if form.is_valid():
			customer_location.save()
			return redirect('core:home')
	return render(request, 'orders/edit_entree.html')


def submit_order(request, user_id):
	user = Account.objects.get(id=user_id)
	context = {}
	return render(request, 'orders/submit_order.html', context)







