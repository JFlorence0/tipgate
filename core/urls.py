"""Defines URL patterns for tip_gate."""

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
	# Customer update current venue 
	path('update_customer_location/<int:user_id>/', views.update_customer_location, name='update_customer_location'),

	# Venue home page
	path('venue_page/<int:user_id>/', views.venue_page, name='venue_page'),
	# Build Menu Page
	path('build_menu/<int:user_id>/', views.build_menu, name='build_menu'),
	# Add a main course to the menu
	path('add_main_course/<int:user_id>/', views.add_main_course, name='add_main_course'),
	# Add video to a main course item
	path('add_main_course_video/<int:user_id>/', views.add_main_course_video, name='add_main_course_video'),
	# View Entree
	path('entree_view/<int:entree_id>/', views.entree_view, name='entree_view'),

]