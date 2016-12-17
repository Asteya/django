from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cause,Story
from django.core.urlresolvers import reverse_lazy
# Create your views here.
class IndexView(generic.ListView):
	
	template_name = 'story/index.html'
	def get_queryset(self):
		return Story.objects.all()
		
class DetailView(generic.DetailView):
	model = Story
	template_name = 'story/detail.html'
 	


class StoryCreate(CreateView):
	
	model =Story
	fields = ['ngo','cause','story_title','cover','body']	

class StoryUpdate(UpdateView):
	
	model =Story
	fields = ['ngo','cause','story_title','cover','body']	

class StoryDelete(DeleteView):
	model = Story
	success_url = reverse_lazy('story:index')