from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Cause,Story,Ngo,Talk
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import Userform

# Create your views here.


######Story#######
class IndexView(generic.ListView):
	
	template_name = 'story/index.html'
	context_object_name = 'story_list'
	def get_queryset(self):
		return Story.objects.all()
		
class DetailView(generic.DetailView):
	model = Story
	template_name = 'story/detail.html'

class AppView(generic.ListView):
	template_name='app/index.html'
	model=Story


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
					current_user = request.user
					return redirect("story:index")

		return render(request,self.template_name,{'form':form})

class ProfileView(UpdateView):
	form_class = Userform
	template_name = 'ngo/profile.html'

	def get(self,request):
		form =self.form_class(None)
		return render(request,self.template_name,{'form': form})

	def post(self,request):
		form =self.form_class(request.POST)

		if request.user.is_authenticated:
			if request.user.is_active:
				if request.user == ngo.user:
					model = Ngo
					fields = ['cause','ngo_name','ngo_pic','body']





#####Talk#######

class TalkIndexView(generic.ListView):
	
	template_name = 'talks/index.html'
	talk_object_name = 'talk_list'
	def get_queryset(self):
		return Talk.objects.all()
		
class TalkDetailView(generic.DetailView):
	model = Talk
	template_name = 'talks/detail.html'





class TalkCreate(CreateView):
	
	model =Talk
	fields = ['ngo','cause','title','cover','desc','body','date']	

class TalkUpdate(UpdateView):
	
	model =Talk
	fields = ['ngo','cause','title','cover','desc','body','date']	

class TalkDelete(DeleteView):
	model = Talk
	success_url = reverse_lazy('story:talk-index')





######Ngo##########
class NgoIndexView(generic.ListView):
	
	template_name = 'ngos/index.html'
	def get_queryset(self):
		return Ngo.objects.all()
		
class NgoDetailView(generic.DetailView):
	model = Ngo
	template_name = 'ngos/detail.html'




class NgoUpdate(UpdateView):
		
		def get(self,request):
			current_user = self.request.user
			if current_user.id == ngo.user:
				model = Ngo
				fields = ['cause','ngo_name','ngo_pic','body']
			else:
				pass

						

class NgoDelete(DeleteView):
	model = Ngo
	success_url = reverse_lazy('story:talk-index')




########Sponsor##########

#class SponsorIndexView(generic.ListView):
	
#	template_name = 'sponsors/index.html'
#	def get_queryset(self):
#		return Sponsor.objects.all()
		
#class SponsorDetailView(generic.DetailView):
#	model = Sponsor
#	template_name = 'sponsors/detail.html'





#class SponsorCreate(CreateView):
	
#	model =Sponsor
#	fields = ['ngo','cause','story_title','cover','body']	

#class SponsorUpdate(UpdateView):
	
#	model =Sponsor
#	fields = ['ngo','cause','story_title','cover','body']	

#class SponsorDelete(DeleteView):
#	model = Sponsor
#	success_url = reverse_lazy('story:sponsor-index')


#######Market###########
#class ProductIndexView(generic.ListView):
	
#	template_name = 'market/index.html'
#	def get_queryset(self):
#		return Talk.objects.all()
		
#class TalkDetailView(generic.DetailView):
#	model = Product
#	template_name = 'market/detail.html'






#class ProductCreate(CreateView):
	

#	model =Product
#	fields = ['ngo','cause','story_title','cover','body']	

#class ProductUpdate(UpdateView):
	
#	model =Product
#	fields = ['ngo','cause','story_title','cover','body']	

#class ProductDelete(DeleteView):
#	model = Product
#	success_url = reverse_lazy('story:product-index')