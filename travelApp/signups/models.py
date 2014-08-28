from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.

class SignUp(models.Model):
	first_name = models.CharField(max_length=120, null=True, blank=True)
	last_name = models.CharField(max_length=120, null=True, blank=True)
	email = models.EmailField()
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return smart_unicode(self.email)



class Search(models.Model):
	query = models.CharField(max_length=120, null=False, blank=False)

	def __unicode__(self):
		return smart_unicode(self.query)