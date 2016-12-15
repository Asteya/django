from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Cause(models.Model):
	cause_title = models.CharField(max_length=250)
	cause_cover = models.CharField(max_length=1000)
	body = models.CharField(max_length=2000)

	def __str__(self):
		return self.cause_title 

class Ngo(models.Model):
	cause = models.ForeignKey(Cause, on_delete=models.CASCADE)

	ngo_name = models.CharField(max_length=500)
	ngo_pic = models.CharField(max_length=1000)
	body = models.CharField(max_length=2000)
	def __str__(self):
		return self.ngo_name 

class Story(models.Model):
	ngo = models.ForeignKey(Ngo, on_delete=models.CASCADE)
	cause = models.ForeignKey(Cause, on_delete=models.CASCADE)
	
	story_title = models.CharField(max_length=250)
	cover = models.CharField(max_length=1000)
	body = models.CharField(max_length=2000)
	def __str__(self):
		return self.story_title + '-' 




#class Product(models.Model):

#class Sponsor(models.Model):

#class POBox(models.Model):

#class Ngo(models.Model):

#class User(models.Model):