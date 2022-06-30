"""Defines URL patterns for tip_gate server side."""

from django.urls import path, include

from . import views

app_name = 'server'
urlpatterns = [
	# Server Home Page
	path('', views.home_server, name='home_server'),
	# Server Registration Page
	path('register_server/', views.register_server, name='register_server'),
	# Server Login page
	path('authenticate_server/', views.authenticate_server, name='authenticate_server'),
	# Logout Server
	path('logged_out', views.logged_out, name='logged_out'),
	]