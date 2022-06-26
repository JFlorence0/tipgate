from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from core.models import Venue, CustomerLocation, Menu

# Register your models here.
class AccountAdmin(UserAdmin):
	list_display = ('email', 'username', 'is_venue', 'date_joined', 'first_name', 'last_name','last_login')
	search_fields = ('email', 'username','first_name', 'last_name')
	readonly_fields = ('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Account, AccountAdmin)
admin.site.register(Venue)
admin.site.register(CustomerLocation)
admin.site.register(Menu)