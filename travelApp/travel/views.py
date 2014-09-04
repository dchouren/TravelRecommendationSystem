from itertools import chain
import json
import os
import subprocess


from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import (render, render_to_response,
	RequestContext, HttpResponseRedirect, get_object_or_404,
	HttpResponse)
from django.template import loader, Context

# Create your views here.

def index(request):

	searches = None
	return render(request, 'index.html')
	# searches = Search.objects.exclude(query__isnull=True)

		# all_cities = AllCities.objects.all()

		# # Search.get_valid_searches()


		# valid_searches = []
		# for p in searches:
		#     for d in all_cities.filter(cityString=p.query):
		#        valid_searches.append(d)

		# left_searches = []
		# right_searches = []

		# for i in range(0, len(valid_searches)):
		# 	if i % 2 == 0:
		# 		left_searches.append(valid_searches[i])
		# 	else:
		# 		right_searches.append(valid_searches[i])

		# if request.method == 'POST':
		# 	searchform = SearchForm(request.POST)

		# 	if searchform.is_valid():
		# 		save_it = searchform.save(commit=False)
		# 		save_it.save()

		# 		this_search = [save_it.query]
		# 		# messages.success(request, this_search)

		# 		print 'same page'
		# 		return HttpResponse(json.dumps({'this_search': this_search}))
		# else:
		# 	searchform = SearchForm(request.POST)
		# 	print 'here'
		# return render(request, 'search.html', {'searches': valid_searches,
		# 	'searchform': searchform, 'left_searches': left_searches,
		# 	'right_searches': right_searches, 'all_cities': all_cities})

# @csrf_exempt
def recommend(request):


	citiesQuery = json.loads(request.body)
	citiesVector = ""

	for i in range(0, len(citiesQuery)):
		cities = citiesQuery[i]
		citiesVector += str(cities['text']) + "\n"

	p1 = subprocess.Popen(['java', '-jar', 'TravelRecommender.jar',
			citiesVector], stdout=subprocess.PIPE)

	output = p1.communicate()[0]
	p1.kill

	print output

	cities_json = []
	count = 0
	areas = []

	for city in output.split('\n'):
		if city == None or city =="":
			continue
		if count == 5:
			break

		area = city.split(', ')[1] # most of time country, 
								# sometimes will be state or provice

		if area not in areas:
			areas.append(area)

			cities_json.append({'city': city})
			count += 1
		

	# context = json.dumps({'recommendations': output})

	print cities_json
	return HttpResponse(json.dumps(cities_json))
	# r = requests.post('index', data=context)

	# return render(request, 'index.html', context)
	# return render_to_response('recommend.html', context)