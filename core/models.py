from django.db import models
from users.models import Account

import string
import random

# Create your models here.
class Venue(models.Model):
	owner = models.ForeignKey(Account, on_delete=models.CASCADE)
	venue_name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=30)
	# state = models.CharField(max_length=2, choices=STATE_CHOICES, null=True, blank=True)
	zipcode = models.CharField(max_length=5)

	def __str__(self):
		return f"{self.venue_name}"


class CustomerLocation(models.Model):
	VENUE_CHOICES = tuple([(venue.venue_name,venue.venue_name) for venue in Venue.objects.all()])
	customer = models.OneToOneField(Account, on_delete=models.CASCADE)
	location = models.CharField(max_length=100, choices=VENUE_CHOICES)

	def __str__(self):
		return f"{self.location}"

class Menu(models.Model):
	menu_owner = models.OneToOneField(Venue, on_delete=models.CASCADE)


	def __str__(self):
		return f"{self.id}"

class MainCourse(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	description = models.TextField(null=True)

	def __str__(self):
		return f"{self.name}"

class SideDish(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	description = models.TextField(null=True)

	def __str__(self):
		return f"{self.name}"

class Drink(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	description = models.TextField(null=True)

	def __str__(self):
		return f"{self.name}"

class MainCourseIngredient(models.Model):
	item = models.ForeignKey(MainCourse, on_delete=models.CASCADE)
	ingredient = models.CharField(max_length=30)
	note_about_ingredient = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return f"{self.ingredient}"

class SideDishIngredient(models.Model):
	item = models.ForeignKey(SideDish, on_delete=models.CASCADE)
	ingredient = models.CharField(max_length=30)
	note_about_ingredient = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return f"{self.ingredient}"

class DrinkIngredient(models.Model):
	item = models.ForeignKey(Drink, on_delete=models.CASCADE)
	ingredient = models.CharField(max_length=30)
	note_about_ingredient = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return f"{self.ingredient}"

class ServerLocation(models.Model):
	VENUE_CHOICES = tuple([(venue.venue_name,venue.venue_name) for venue in Venue.objects.all()])
	server = models.OneToOneField(Account, on_delete=models.CASCADE)
	location = models.CharField(max_length=100, choices=VENUE_CHOICES)

	def __str__(self):
		return f"{self.location}"









