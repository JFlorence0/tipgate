"""Defines URL patterns for tip_gate."""

from django.urls import path, include

from . import views

app_name = 'core'
urlpatterns = [
	# Home page
	path('', views.home, name='home'),

	# Manage menus
	path('manage_menus/<int:user_id>/', views.manage_menus, name='manage_menus'),

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
	path('create_base_menu/<int:user_id>/', views.create_base_menu, name='create_base_menu'),

	# Add a main course to the menu
	path('add_main_course/<int:user_id>/', views.add_main_course, name='add_main_course'),
	# Add video to a main course item
	path('add_main_course_video/<int:entree_id>/', views.add_main_course_video, name='add_main_course_video'),
	# Edit a main course
	path('edit_main_course/<int:entree_id>/', views.edit_main_course, name='edit_main_course'),
	# Remove a main course item
	path('remove_main_course/<int:entree_id>/', views.remove_main_course, name='remove_main_course'),
	# View Entree
	path('entree_view/<int:entree_id>/', views.entree_view, name='entree_view'),

	# Add a side dish to the menu
	path('add_side_dish/<int:user_id>/', views.add_side_dish, name='add_side_dish'),
	# Add video to a side dish item
	path('add_side_dish_video/<int:side_id>/', views.add_side_dish_video, name='add_side_dish_video'),
	# Edit a side dish
	path('edit_side_dish/<int:side_id>/', views.edit_side_dish, name='edit_side_dish'),

	# Add a drink to the menu
	path('add_drink/<int:user_id>/', views.add_drink, name='add_drink'),
	# Add video to a drink item
	path('add_drink_video/<int:drink_id>/', views.add_drink_video, name='add_drink_video'),
	# Edit a drink
	path('edit_drink/<int:drink_id>/', views.edit_drink, name='edit_drink'),

	# Add Video To Items
	path('edit_menu/<int:user_id>/', views.edit_menu, name='edit_menu'),

	# Create a custom menu
	path('create_custom_menu/<int:user_id>', views.create_custom_menu, name='create_custom_menu'),
	# View the custom menu
	path('edit_custom_menu/<int:user_id>/', views.edit_custom_menu, name='edit_custom_menu'),
	# Add entree to custom menu
	path('add_custom_entree/<int:user_id>/', views.add_custom_entree, name='add_custom_entree'),
	# Edit custom entree
	path('edit_custom_entree/<int:entree_id>/', views.edit_custom_entree, name='edit_custom_entree'),
	# Add video to custom entree
	path('add_custom_entree_video/<int:entree_id>/', views.add_custom_entree_video, name='add_custom_entree_video'),


	# Add side to custom menu
	path('add_custom_side/<int:user_id>/', views.add_custom_side, name='add_custom_side'),
	# Edit custom side
	path('edit_custom_side/<int:side_id>/', views.edit_custom_side, name='edit_custom_side'),
	# Add video to custom entree
	path('add_custom_side_video/<int:side_id>/', views.add_custom_side_video, name='add_custom_side_video'),
	# Add drink to custom menu
	path('add_custom_drink/<int:user_id>/', views.add_custom_drink, name='add_custom_drink'),
	# Edit custom drink
	path('edit_custom_drink/<int:drink_id>/', views.edit_custom_drink, name='edit_custom_drink'),
	# Add video to custom entree
	path('add_custom_drink_video/<int:drink_id>/', views.add_custom_drink_video, name='add_custom_drink_video'),

	# Select a custom menu to view by selecting the location
	path('select_custom_menu/<int:user_id>/', views.select_custom_menu, name='select_custom_menu'),


















]