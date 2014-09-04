from django.contrib import admin

# Register your models here.
# from .models import Search
# from .models import AllCities


# class SearchAdmin(admin.ModelAdmin):
# 	class Meta:
# 		model = Search

# class AllCitiesAdmin(admin.ModelAdmin):
# 	class Meta:
# 		model = AllCities

# admin.site.register(Search, SearchAdmin)
# admin.site.register(AllCities, AllCitiesAdmin)


from .models import AllCities

class AllCitiesAdmin(admin.ModelAdmin):
	class Meta:
		model = AllCities

admin.site.register(AllCities, AllCitiesAdmin)




from .models import AllMembers

class AllMembersAdmin(admin.ModelAdmin):
	class Meta:
		model = AllMembers

admin.site.register(AllMembers, AllMembersAdmin)




from .models import MemberCityPairs

class MemberCityPairsAdmin(admin.ModelAdmin):
	class Meta:
		model = MemberCityPairs

admin.site.register(MemberCityPairs, MemberCityPairsAdmin)