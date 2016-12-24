from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# Create your models here.

class Cause(models.Model):
	cause_title = models.CharField(max_length=250)
	cause_cover = models.CharField(max_length=1000)
	body = models.CharField(max_length=2000)

	def __str__(self):
		return self.cause_title 

class Ngo(models.Model):
	cause = models.ForeignKey(Cause, on_delete=models.CASCADE)
	user = models.ForeignKey(User, unique=True)
	ngo_name = models.CharField(max_length=500)
	ngo_pic = models.FileField()
	ngo_cover = models.FileField()
	address = models.CharField(max_length=500 ,null='true')
	website = models.CharField(max_length=200,null='true')
	founded_date = models.DateField(null='true')
	contact = models.CharField(max_length=500,null='true')
	awards = models.CharField(max_length=1000,null='true')
	vision = models.CharField(max_length=1000,null='true')
	mission = models.CharField(max_length=1000,null='true')
	history = models.CharField(max_length=2000,null='true')
	body = models.CharField(max_length=2000,null='true')
	
	def get_absolute_url(self):
		return reverse('story:detail', kwargs={'pk': self.pk})

	def __str__(self):
		return self.ngo_name 

class Story(models.Model):
	ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
	cause = models.ForeignKey(Cause, on_delete=models.CASCADE)
	
	story_title = models.CharField(max_length=250)
	cover = models.FileField()
	body = models.CharField(max_length=2000)
	
	def get_absolute_url(self):
		return reverse('story:detail', kwargs={'pk': self.pk})


	def __str__(self):
		return self.story_title + '-' 

#class Sponsor(models.Model):
	

class Talk(models.Model):
	ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
	#sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
	cause = models.ForeignKey(Cause, on_delete=models.CASCADE)
	title = models.CharField(max_length=250)
	cover = models.FileField()
	desc = models.CharField(max_length=250)
	body = models.CharField(max_length=250)
	date =models.DateField()

	def get_absolute_url(self):
		return reverse('story:talk-detail', kwargs={'pk': self.pk})


	def __str__(self):
		return self.title + '-' 



#class Product(models.Model):
#	title = models.CharField(max_length=250)
#	desc = models.CharField(max_length=250)
#	body = models.CharField(max_length=250)
#	cover = models.FileField()
#	price = models.



#class POBox(models.Model):






