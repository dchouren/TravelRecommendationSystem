from django import forms


from .models import Search


class SearchForm(forms.ModelForm):
	# query = forms.ModelChoiceField(  required=True, queryset=ships.models.Authority.objects.all() , ) 
	# query = forms.CharField(widget=forms.TextInput(attrs={'size':'45'}))
	class Meta:
		model = Search


# class SignUpForm(forms.ModelForm):
# 	class Meta:
# 		model = SignUp