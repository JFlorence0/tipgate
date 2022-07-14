from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from core.models import Venue, CustomerLocation, Menu, MainCourse, CustomMenu
from core.models import ServerLocation, MainCourseVideo, SideDish, SideDishVideo
from core.models import Drink, DrinkVideo, CustomMenu, CustomEntree, CustomSideDish, CustomDrink

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
admin.site.register(ServerLocation)
admin.site.register(MainCourse)
admin.site.register(MainCourseVideo)
admin.site.register(SideDish)
admin.site.register(SideDishVideo)
admin.site.register(Drink)
admin.site.register(DrinkVideo)

admin.site.register(CustomMenu)
admin.site.register(CustomEntree)
admin.site.register(CustomSideDish)
admin.site.register(CustomDrink)