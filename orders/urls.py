""" URL patterns for customer orders. """
from django.urls import path, include

from . import views

app_name = 'orders'
urlpatterns = [
	# Place order for customers
	path('place_order/<int:user_id>/', views.place_order, name='place_order'),

	# Customer final order submission.
	path('submit_order/<int:user_id>/', views.submit_order, name='submit_order'),

	# Customer add/edit ingredients.
	path('edit_ingredients/<int:user_id>/', views.edit_ingredients, name='edit_ingredients'),

	# Customer edit entree ingredients.
	path('edit_entree/<int:user_id>', views.edit_entree, name='edit_entree'),
	]