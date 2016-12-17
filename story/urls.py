from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = "story"

urlpatterns = [
    
    url(r'^$', views.IndexView.as_view(), name = 'index'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
    #story/add
    url(r'^add/$',views.StoryCreate.as_view(), name='add-story'),
    url(r'^edit/(?P<pk>[0-9]+)/$',views.StoryUpdate.as_view(), name='edit-story'),
    url(r'^delete/(?P<pk>[0-9]+)/$',views.StoryDelete.as_view(), name='delete-story'),



]
