from django.shortcuts import render, redirect

from users.models import Account
from core.models import CustomerLocation, CustomerOrder
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
			return redirect('orders:place_order', user_id)

	context = {'user':user, 'customer_location':customer_location, 'form':form}
	return render(request, 'orders/place_order.html', context)