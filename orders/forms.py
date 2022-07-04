from django import forms
from core.models import CustomerOrder

class CustomerOrderForm(forms.ModelForm):
	
	class Meta:
		model = CustomerOrder
		fields = ('venue', 'entree', 'side', 'drink')

