"""Defines URL patterns for tip_gate server side."""

from django.urls import path, include

from . import views

app = 'server'
urlpatterns = [
	# Server Home Page
	path('', views.home_server, name='home_server'),
	]