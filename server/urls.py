"""Defines URL patterns for tip_gate server side."""

from django.urls import path, include

from . import views

app_name = 'server'
urlpatterns = [
	# Server Home Page
	path('', views.home_server, name='home_server'),
	# Server Registration Page
	path('register_server/', views.register_server, name='register_server'),
	]