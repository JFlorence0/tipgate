from django import forms
from .models import Venue, CustomerLocation, Menu, MainCourse, SideDish, Drink

class VenueForm(forms.ModelForm):

	class Meta:
		model = Venue
		fields = ('venue_name', 'address', 'city', 'zipcode')

class CustomerLocationForm(forms.ModelForm):

	class Meta:
		model = CustomerLocation
		fields = ('location',)

class MenuForm(forms.ModelForm):

	class Meta:
		model = Menu
		fields = ('menu_owner',)

class MainCourseForm(forms.ModelForm):

	class Meta:
		model = MainCourse
		fields = ('name', 'description')

class SideDishForm(forms.ModelForm):

	class Meta:
		model = SideDish
		fields = ('name', 'description')
class DrinkForm(forms.ModelForm):

	class Meta:
		model = Drink
		fields = ('name', 'description')






