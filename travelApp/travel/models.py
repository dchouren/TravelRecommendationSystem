from urlparse import urlparse

from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User

# Create your models here.


class Search(models.Model):
	query = models.CharField(max_length=120, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	# moderator = models.ForeignKey(User)

	def __unicode__(self):
		return smart_unicode(self.query)


	# def get_valid_searches():
	# 	all_cities = AllMembers

	# 	return len(all_cities)



# class SignUp(models.Model):
# 	first_name = models.CharField(max_length=120, null=False, blank=False)
# 	last_name = models.CharField(max_length=120, null=False, blank=False)
# 	email = models.Email()



# holds all of the cities in mc model
class AllCities(models.Model):
	cityString = models.CharField(max_length=120, unique=True, null=False, blank=False)

	def __unicode__(self):
		return smart_unicode(self.cityString)



class AllMembers(models.Model):
	member = models.CharField(max_length=120, unique=True, null=False, blank=False)

	def __unicode__(self):
		return smart_unicode(self.member)



class memberCityPairs(models.Model):
	memberId = models.ForeignKey(AllMembers)
	cityId = models.ForeignKey(AllCities)