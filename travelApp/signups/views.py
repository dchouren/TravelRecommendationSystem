
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect


# Create your views here.

from .forms import SignUpForm
from .forms import SearchForm


def addlocation(request):

	searchform = SearchForm(request.POST or None)

	if searchform.is_valid():
		save_it = searchform.save(commit=False)
		save_it.save()

		this_search = [save_it.query]
		messages.success(request, this_search)

	return render_to_response("signup.html", locals(),
		context_instance=RequestContext(request))



def home(request):

	searchform = SearchForm(request.POST or None)

	if searchform.is_valid():
		save_it = searchform.save(commit=False)
		save_it.save()

		this_search = [save_it.query]
		messages.success(request, this_search)




	# form = SignUpForm(request.POST or None)

	# if form.is_valid():
	# 	save_it = form.save(commit=False)
	# 	save_it.save();
	# 	subject = 'thank you'
	# 	message = 'welcome'
	# 	from_email = settings.EMAIL_HOST_USER
	# 	to_list = [save_it.email]

	# 	send_mail(subject, message, from_email, to_list, fail_silently=False)

	# 	messages.success(request, 'Thank you for joining')
	# 	return HttpResponseRedirect('/thank-you/')

	return render_to_response("signup.html", locals(),
		context_instance=RequestContext(request))
