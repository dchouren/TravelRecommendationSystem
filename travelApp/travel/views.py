from itertools import chain

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect, get_object_or_404

# Create your views here.

from .forms import SearchForm

from travel.models import Search
# from travel
from travel.models import AllCities



def home(request):

	searches = None
	searches = Search.objects.exclude(query__isnull=True)

	all_cities = AllCities.objects.all()

	# Search.get_valid_searches()


	valid_searches = []
	for p in searches:
	    for d in all_cities.filter(cityString=p.query):
	       valid_searches.append(d)

	left_searches = []
	right_searches = []

	for i in range(0, len(valid_searches)):
		if i % 2 == 0:
			left_searches.append(valid_searches[i])
		else:
			right_searches.append(valid_searches[i])

	if request.method == 'POST':
		searchform = SearchForm(request.POST)

		if searchform.is_valid():
			save_it = searchform.save(commit=False)
			save_it.save()

			this_search = [save_it.query]
			messages.success(request, this_search)

			return HttpResponseRedirect('')
	else:
		searchform = SearchForm(request.POST)


	return render(request, 'search.html', {'searches': valid_searches,
		'searchform': searchform, 'left_searches': left_searches,
		'right_searches': right_searches, 'all_cities': all_cities})



	# previous_queries = get_object_or_404()


	# return render_to_response("search.html", locals(),
	# 	context_instance=RequestContext(request))



def previous_searches():
	previous_searches = Search.objects.all().order_by('-created_at')



def search(request):

	searchform = SearchForm(request.POST or None)

	if searchform.is_valid():
		save_it = searchform.save(commit=False)
		save_it.save()

		this_search = [save_it.query]
		messages.success(request, this_search)


	previous = previous_searches()
	response = '''
	<html>
	<head>
		<title>Searches</title>
	</head>
	<body>
		<ol>
		%s
		</ol>
	</body>
	</html>
	''' % '\n'.join(['<li>%s</li>' % search.query for search in previous])

	return HttpResponse(response)

	# return render_to_response("search.html", locals(),
		# context_instance=RequestContext(request))
