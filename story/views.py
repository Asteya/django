from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cause,Story
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import Userform

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


class UserFormView(View):
	form_class = Userform
	template_name = 'story/registration_form.html'

	#get form request
	def get(self,request):
		form =self.form_class(None)
		return render(request,self.template_name,{'form': form})


	def post(self,request):
		form =self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			# cleaned  data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user= authenticate(username=username,password=password)

			if user is not None:
				if user.is_active:
					login(request,user)
					return redirect("story:index")

		return render(request,self.template_name,{'form':form})