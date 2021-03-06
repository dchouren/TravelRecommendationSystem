from itertools import chain
import json
import os
import subprocess
from subprocess import Popen, PIPE, STDOUT


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




# @csrf_exempt
def recommend(request):

	citiesQuery = json.loads(request.body)
	citiesVector = "NEXT SEARCH\n"
	# citiesVector = ""

	for i in range(0, len(citiesQuery)):
		cities = citiesQuery[i]
		citiesVector += str(cities['text']) + "\n"

	citiesVector += "PREDICT\n"

	print citiesVector

	# print "here"
	# # if jar has not been started yet, actually start it
	# if not 'recommender_jar' in request.session:
	# 	print 'first time'
		
	# 	request.session['recommender_jar'] = subprocess.Popen(['java', 
	# 		'-jar', 'CyclicTravelRecommender.jar'
	# 		], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	# 	print "here2"
	# else:
	# 	print "here3"
	# 	recommender_jar.stdin.write(citiesVector);
	# 	print "here4"
	
	
	recommender_jar = subprocess.Popen(['java', '-jar',
		'TravelRecommender2.jar', citiesVector,
		], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
	# output = recommender_jar.communicate()[0]
	
	# recommender_jar.stdin.write(citiesVector)
	# print "here5"
	# recommender_jar = request.session.get('recommender_jar')

	output = recommender_jar.communicate()[0]

	# print "output: "
	print output
	# print "output end"

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
		
	# print cities_json
	return HttpResponse(json.dumps(cities_json))