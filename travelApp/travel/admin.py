from django.contrib import admin

# Register your models here.
from .models import Search
from .models import AllCities


class SearchAdmin(admin.ModelAdmin):
	class Meta:
		model = Search

class AllCitiesAdmin(admin.ModelAdmin):
	class Meta:
		model = AllCities

admin.site.register(Search, SearchAdmin)
admin.site.register(AllCities, AllCitiesAdmin)
