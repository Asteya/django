from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<story_id>[0-9]+)/$', views.story, name = 'story'),


]
