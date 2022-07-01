""" URL patterns for customer orders. """
from django.urls import path, include

from . import views

app_name = 'orders'
urlpatterns = [
	# Place order for customers
	path('place_order/<int:user_id>', views.place_order, name='place_order'),
	]