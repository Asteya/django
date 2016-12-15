from django.shortcuts import render, get_object_or_404

from .models import Cause,Story

# Create your views here.

def index(request):
	all_stories = Story.objects.all()
	context = {	 'all_stories': all_stories }
	return render(request,'story/index.html',context)


def cause(request):
	all_causes = Cause.objects.all()
	html = ''
	for cause in all_causes:
		url = '/cause/'+ str(cause.id) + '/'
		html += '<a href="#">cause_title</a><br>'
	return HttpResponse(html)


def detail(request, story_id):
	story = get_object_or_404(Story,id=story_id)
	return render(request,'story/detail.html',{'story': story})	
