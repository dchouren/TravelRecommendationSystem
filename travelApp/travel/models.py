from urlparse import urlparse

from django.db import models
from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User

# Create your models here.


# class Search(models.Model):
# 	query = models.CharField(max_length=120, null=True, blank=True)
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	# moderator = models.ForeignKey(User)

# 	def __unicode__(self):
# 		return smart_unicode(self.query)


# 	# def get_valid_searches():
# 	# 	all_cities = AllMembers

# 	# 	return len(all_cities)

class AllCities(models.Model):
	cityString = models.CharField(max_length=120, null=False, blank=False)

	def __unicode__(self):
		return smart_unicode(self.cityString)



class AllMembers(models.Model):
	memberString = models.CharField(max_length=120, null=False, blank=False)

	def __unicode__(self):
		return smart_unicode(self.memberString)



class MemberCityPairs(models.Model):
	memberIndex = models.ForeignKey(AllMembers)
	cityIndex = models.ForeignKey(AllCities)

