"""Defines URL patterns for vareaze."""

from django.urls import path, include

from . import views

app_name = 'core'
urlpatterns = [
	# Home page
	path('', views.home, name='home'),
	path('venue_form/<int:user_id>/', views.venue_form, name='venue_form'),
	path('customer_location/<int:user_id>', views.customer_location, name='customer_location'),
]