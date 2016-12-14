from django.shortcuts import render
from django.http import HttpResponse
from .models import Cause,Story


# Create your views here.

def index(request):
	all_stories = Story.objects.all()
	html = ''
	for story in all_stories:
		url = '/story/'+ str(story.id) + '/'
		html += '<a href="'+ url + '">' + story.story_title + '</a><br>'
	return HttpResponse(html)


def cause(request):
	all_causes = Cause.objects.all()
	html = ''
	for cause in all_causes:
		url = '/cause/'+ str(cause.id) + '/'
		html += '<a href="#">cause_title</a><br>'
	return HttpResponse(html)


def story(request, story_id):
	return HttpResponse("hi")	