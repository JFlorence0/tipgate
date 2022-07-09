from django import forms
from .models import Venue, CustomerLocation, Menu
from .models import MainCourse, MainCourseVideo

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





