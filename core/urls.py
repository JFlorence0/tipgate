"""Defines URL patterns for vareaze."""

from django.urls import path, include

from . import views

app_name = 'core'
urlpatterns = [
	# Home page
	path('', views.home, name='home'),
	# Add a venue to an owner
	path('venue_form/<int:user_id>/', views.venue_form, name='venue_form'),
	# Customer venue choice
	path('customer_location/<int:user_id>', views.customer_location, name='customer_location'),
	# Venue home page
	path('venue_page/<int:user_id>/', views.venue_page, name='venue_page'),
	# Build Menu Page
	path('build_menu/<int:user_id>/', views.build_menu, name='build_menu'),
	
]