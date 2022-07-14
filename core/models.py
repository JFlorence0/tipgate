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
	menu_owner = models.OneToOneField(Account, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.menu_owner}"

class MainCourse(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	ingredient1 = models.CharField(max_length=100, null=True, blank=True)
	ingredient2 = models.CharField(max_length=100, null=True, blank=True)
	ingredient3 = models.CharField(max_length=100, null=True, blank=True)
	ingredient4 = models.CharField(max_length=100, null=True, blank=True)
	ingredient5 = models.CharField(max_length=100, null=True, blank=True)
	ingredient6 = models.CharField(max_length=100, null=True, blank=True)
	ingredient7 = models.CharField(max_length=100, null=True, blank=True)
	ingredient8 = models.CharField(max_length=100, null=True, blank=True)
	ingredient9 = models.CharField(max_length=100, null=True, blank=True)
	ingredient10 = models.CharField(max_length=100, null=True, blank=True)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return f"{self.name}"

class MainCourseVideo(models.Model):
	main_course_item = models.ForeignKey(MainCourse, on_delete=models.CASCADE)
	video = models.FileField(upload_to='videos/', null=True, verbose_name="")

	def __str__(self):
		return f"{self.main_course_item}"

class SideDish(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	ingredient1 = models.CharField(max_length=100, null=True, blank=True)
	ingredient2 = models.CharField(max_length=100, null=True, blank=True)
	ingredient3 = models.CharField(max_length=100, null=True, blank=True)
	ingredient4 = models.CharField(max_length=100, null=True, blank=True)
	ingredient5 = models.CharField(max_length=100, null=True, blank=True)
	ingredient6 = models.CharField(max_length=100, null=True, blank=True)
	ingredient7 = models.CharField(max_length=100, null=True, blank=True)
	ingredient8 = models.CharField(max_length=100, null=True, blank=True)
	ingredient9 = models.CharField(max_length=100, null=True, blank=True)
	ingredient10 = models.CharField(max_length=100, null=True, blank=True)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return f"{self.name}"

class SideDishVideo(models.Model):
	side_dish_item = models.ForeignKey(SideDish, on_delete=models.CASCADE)
	video = models.FileField(upload_to='videos/', null=True, verbose_name="")

class Drink(models.Model):
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	ingredient1 = models.CharField(max_length=100, null=True, blank=True)
	ingredient2 = models.CharField(max_length=100, null=True, blank=True)
	ingredient3 = models.CharField(max_length=100, null=True, blank=True)
	ingredient4 = models.CharField(max_length=100, null=True, blank=True)
	ingredient5 = models.CharField(max_length=100, null=True, blank=True)
	ingredient6 = models.CharField(max_length=100, null=True, blank=True)
	ingredient7 = models.CharField(max_length=100, null=True, blank=True)
	ingredient8 = models.CharField(max_length=100, null=True, blank=True)
	ingredient9 = models.CharField(max_length=100, null=True, blank=True)
	ingredient10 = models.CharField(max_length=100, null=True, blank=True)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return f"{self.name}"

class DrinkVideo(models.Model):
	drink_item = models.ForeignKey(Drink, on_delete=models.CASCADE)
	video = models.FileField(upload_to='videos/', null=True, verbose_name="")

	def __str__(self):
		return f"{self.side_dish_item}"


class ServerLocation(models.Model):
	VENUE_CHOICES = tuple([(venue.venue_name,venue.venue_name) for venue in Venue.objects.all()])
	server = models.OneToOneField(Account, on_delete=models.CASCADE)
	location = models.CharField(max_length=100, choices=VENUE_CHOICES)

	def __str__(self):
		return f"{self.location}"

class CustomerOrder(models.Model):
	VENUE_CHOICES = tuple([(venue.venue_name,venue.venue_name) for venue in Venue.objects.all()])
	customer = models.ForeignKey(Account, on_delete = models.CASCADE)
	venue = models.CharField(max_length=100, choices = VENUE_CHOICES)
	entree = models.CharField(max_length=100, null=True)
	drink = models.CharField(max_length=100, null=True)
	date_added = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return f"{self.entree}, {self.drink}"

class CustomMenu(models.Model):
	custom_menu_owner = models.OneToOneField(Venue, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.custom_menu_owner}"

class CustomEntree(models.Model):
	custom_menu = models.ForeignKey(CustomMenu, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	ingredient1 = models.CharField(max_length=100, null=True, blank=True)
	ingredient2 = models.CharField(max_length=100, null=True, blank=True)
	ingredient3 = models.CharField(max_length=100, null=True, blank=True)
	ingredient4 = models.CharField(max_length=100, null=True, blank=True)
	ingredient5 = models.CharField(max_length=100, null=True, blank=True)
	ingredient6 = models.CharField(max_length=100, null=True, blank=True)
	ingredient7 = models.CharField(max_length=100, null=True, blank=True)
	ingredient8 = models.CharField(max_length=100, null=True, blank=True)
	ingredient9 = models.CharField(max_length=100, null=True, blank=True)
	ingredient10 = models.CharField(max_length=100, null=True, blank=True)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return f"{self.name}"

class CustomSideDish(models.Model):
	custom_menu = models.ForeignKey(CustomMenu, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	ingredient1 = models.CharField(max_length=100, null=True, blank=True)
	ingredient2 = models.CharField(max_length=100, null=True, blank=True)
	ingredient3 = models.CharField(max_length=100, null=True, blank=True)
	ingredient4 = models.CharField(max_length=100, null=True, blank=True)
	ingredient5 = models.CharField(max_length=100, null=True, blank=True)
	ingredient6 = models.CharField(max_length=100, null=True, blank=True)
	ingredient7 = models.CharField(max_length=100, null=True, blank=True)
	ingredient8 = models.CharField(max_length=100, null=True, blank=True)
	ingredient9 = models.CharField(max_length=100, null=True, blank=True)
	ingredient10 = models.CharField(max_length=100, null=True, blank=True)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return f"{self.name}"

class CustomDrink(models.Model):
	custom_menu = models.ForeignKey(CustomMenu, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	ingredient1 = models.CharField(max_length=100, null=True, blank=True)
	ingredient2 = models.CharField(max_length=100, null=True, blank=True)
	ingredient3 = models.CharField(max_length=100, null=True, blank=True)
	ingredient4 = models.CharField(max_length=100, null=True, blank=True)
	ingredient5 = models.CharField(max_length=100, null=True, blank=True)
	ingredient6 = models.CharField(max_length=100, null=True, blank=True)
	ingredient7 = models.CharField(max_length=100, null=True, blank=True)
	ingredient8 = models.CharField(max_length=100, null=True, blank=True)
	ingredient9 = models.CharField(max_length=100, null=True, blank=True)
	ingredient10 = models.CharField(max_length=100, null=True, blank=True)
	description = models.TextField(null=True, blank=True)

	def __str__(self):
		return f"{self.name}"

class CustomEntreeVideo(models.Model):
	custom_entree = models.ForeignKey(CustomEntree, on_delete=models.CASCADE)
	video = models.FileField(upload_to='videos/', null=True, verbose_name="")

	def __str__(self):
		return f"{self.custom_entree}"

class CustomSideDishVideo(models.Model):
	custom_side_dish = models.ForeignKey(CustomSideDish, on_delete=models.CASCADE)
	video = models.FileField(upload_to='videos/', null=True, verbose_name="")

	def __str__(self):
		return f"{self.custom_side_dish}"

class CustomDrinkVideo(models.Model):
	custom_drink = models.ForeignKey(CustomDrink, on_delete=models.CASCADE)
	video = models.FileField(upload_to='videos/', null=True, verbose_name="")

	def __str__(self):
		return f"{self.custom_drink}"




