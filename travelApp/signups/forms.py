from django import forms


from .models import SignUp
from .models import Search

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp

class SearchForm(forms.ModelForm):
	class Meta:
		model = Search