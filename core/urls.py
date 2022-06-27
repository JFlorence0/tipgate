"""Defines URL patterns for vareaze."""

from django.urls import path, include

from . import views

app_name = 'core'
urlpatterns = [
	# Home page
	path('', views.home, name='home'),

	# View the venue's menu, POV of Venue
	path('venue_menu_view/<int:user_id>/', views.venue_menu_view, name='venue_menu_view'),
	
	# Add a venue to an owner
	path('venue_form/<int:user_id>/', views.venue_form, name='venue_form'),
	# Customer venue choice
	path('customer_location/<int:user_id>', views.customer_location, name='customer_location'),
	# Venue home page
	path('venue_page/<int:user_id>/', views.venue_page, name='venue_page'),
	# Build Menu Page
	path('build_menu/<int:user_id>/', views.build_menu, name='build_menu'),
	# Add a main course to the menu
	path('add_main_course/<int:user_id>/', views.add_main_course, name='add_main_course'),
	# Add a side dish to the menu
	path('add_side_dish/<int:user_id>/', views.add_side_dish, name='add_side_dish'),
	# Add a drink to the menu
	path('add_drink/<int:user_id>/', views.add_drink, name='add_drink'),
	
	# Add an ingredient to the main course
	path('add_main_course_ingredient/<int:user_id>/', views.add_main_course_ingredient, name='add_main_course_ingredient'),
	# Add an ingredient to the main course
	path('add_side_dish_ingredient/<int:user_id>/', views.add_side_dish_ingredient, name='add_side_dish_ingredient'),
	# Add an ingredient to the main course
	path('add_drink_ingredient/<int:user_id>/', views.add_drink_ingredient, name='add_drink_ingredient'),
]