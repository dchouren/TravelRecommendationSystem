from django.contrib import admin

# Register your models here.
from .models import SignUp
from .models import Search


class SignUpAdmin(admin.ModelAdmin):
	class Meta:
		model = SignUp

class SearchAdmin(admin.ModelAdmin):
	class Meta:
		model = Search

admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Search, SearchAdmin)