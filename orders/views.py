from django.shortcuts import render, redirect

from users.models import Account
from core.models import CustomerLocation

# Create your views here.
def place_order(request, user_id):
	user = Account.objects.get(id=user_id)
	customer_location = [cust.location for cust in CustomerLocation.objects.all() if str(cust.customer) == str(request.user.email)]
	customer_location = customer_location[0]
	context = {'user':user, 'customer_location':customer_location}
	return render(request, 'orders/place_order.html', context)