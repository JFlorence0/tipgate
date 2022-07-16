from django import forms
from .models import (
	Venue, CustomerLocation, Menu, SideDish, Drink, 
	MainCourse, MainCourseVideo, SideDishVideo, DrinkVideo,
	CustomMenu, CustomEntree, CustomSideDish, CustomDrink,
	CustomEntreeVideo, CustomSideDishVideo, CustomDrinkVideo, SelectCustomMenu)


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
		fields = ('name', 'ingredient1', 'ingredient2', 'ingredient3',
		 	'ingredient4', 'ingredient5', 'ingredient6', 'ingredient7',
		 	 'ingredient8', 'ingredient9', 'ingredient10', 'description')

class MainCourseVideoForm(forms.ModelForm):

	class Meta:
		model = MainCourseVideo
		fields = ('main_course_item', 'video')

class SideDishForm(forms.ModelForm):

	class Meta:
		model = SideDish
		fields = ('name', 'ingredient1', 'ingredient2', 'ingredient3',
		 	'ingredient4', 'ingredient5', 'ingredient6', 'ingredient7',
		 	 'ingredient8', 'ingredient9', 'ingredient10', 'description')

class SideDishVideoForm(forms.ModelForm):

	class Meta:
		model = SideDishVideo
		fields = ('side_dish_item', 'video')

class DrinkForm(forms.ModelForm):

	class Meta:
		model = Drink
		fields = ('name', 'ingredient1', 'ingredient2', 'ingredient3',
		 	'ingredient4', 'ingredient5', 'ingredient6', 'ingredient7',
		 	 'ingredient8', 'ingredient9', 'ingredient10', 'description')

class DrinkVideoForm(forms.ModelForm):

	class Meta:
		model = DrinkVideo
		fields = ('drink_item', 'video')

class CustomMenuForm(forms.ModelForm):

	class Meta:
		model = CustomMenu
		fields = ('custom_menu_owner',)
		labels = {'custom_menu_owner': 'Choose Venue'}

class CustomEntreeForm(forms.ModelForm):

	class Meta:
		model = CustomEntree
		fields = ('name', 'ingredient1', 'ingredient2', 'ingredient3',
		 	'ingredient4', 'ingredient5', 'ingredient6', 'ingredient7',
		 	 'ingredient8', 'ingredient9', 'ingredient10', 'description')

class CustomEntreeVideoForm(forms.ModelForm):

	class Meta:
		model = CustomEntreeVideo
		fields = ('custom_entree', 'video')

class CustomSideDishForm(forms.ModelForm):

	class Meta:
		model = CustomSideDish
		fields = ('name', 'ingredient1', 'ingredient2', 'ingredient3',
		 	'ingredient4', 'ingredient5', 'ingredient6', 'ingredient7',
		 	 'ingredient8', 'ingredient9', 'ingredient10', 'description')

class CustomSideDishVideoForm(forms.ModelForm):

	class Meta:
		model = CustomSideDishVideo
		fields = ('custom_side_dish', 'video')

class CustomDrinkForm(forms.ModelForm):

	class Meta:
		model = CustomDrink
		fields = ('name', 'ingredient1', 'ingredient2', 'ingredient3',
		 	'ingredient4', 'ingredient5', 'ingredient6', 'ingredient7',
		 	 'ingredient8', 'ingredient9', 'ingredient10', 'description')

class CustomDrinkVideoForm(forms.ModelForm):

	class Meta:
		model = CustomDrinkVideo
		fields = ('custom_drink', 'video')

class SelectCustomMenuForm(forms.ModelForm):

	class Meta:
		model = SelectCustomMenu
		fields = ('venue', 'owner')


















