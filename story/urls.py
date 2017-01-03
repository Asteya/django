from django.conf.urls import url
from django.contrib import admin
from . import views
from story import views
app_name = "story"

urlpatterns = [
    
    url(r'^$', views.AppView.as_view(), name = 'index'),
    url(r'^today/$', views.IndexView.as_view(), name = 'index-today'),
    url(r'^register/$',views.UserFormView.as_view(),name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),

    url(r'^login/', views.Login),
    url(r'^logout/', views.Logout,name="logout"),

    #story/add
    url(r'^add/$',views.StoryCreate.as_view(), name='add-story'),
    url(r'^edit/(?P<pk>[0-9]+)/$',views.StoryUpdate.as_view(), name='edit-story'),
    url(r'^delete/(?P<pk>[0-9]+)/$',views.StoryDelete.as_view(), name='delete-story'),
   
    #talks/
    url(r'^talks$', views.TalkIndexView.as_view(), name = 'talk-index'),
    url(r'^talks/(?P<pk>[0-9]+)/$', views.TalkDetailView.as_view(), name = 'talk-detail'),

    url(r'^talks/add/$',views.TalkCreate.as_view(), name='add-talk'),
    url(r'^talks/edit/(?P<pk>[0-9]+)/$',views.TalkUpdate.as_view(), name='edit-talk'),
    url(r'^talks/delete/(?P<pk>[0-9]+)/$',views.TalkDelete.as_view(), name='delete-delete'),
   
    #ngos/
    url(r'^ngos$', views.NgoIndexView.as_view(), name = 'ngo-index'),
    url(r'^ngos/(?P<pk>[0-9]+)/$', views.NgoDetailView.as_view(), name = 'ngo-detail'),
   
    url(r'^ngos/edit/(?P<pk>[0-9]+)/$',views.NgoUpdate.as_view(), name='edit-ngo'),
    url(r'^ngos/delete/(?P<pk>[0-9]+)/$',views.NgoDelete.as_view(), name='delete-ngo'),
    
    #sponsors/
   # url(r'^sponsors$', views.SponsorIndexView.as_view(), name = 'sponsor-index'),
   # url(r'^sponsors/(?P<pk>[0-9]+)/$', views.SponsorDetailView.as_view(), name = 'sponsor-detail'),

   # url(r'^sponsors/add/$',views.SponsoCreate.as_view(), name='add-sponsor'),
   # url(r'^sponsors/edit/(?P<pk>[0-9]+)/$',views.SponsorUpdate.as_view(), name='edit-sponsor'),
   # url(r'^sponsors/delete/(?P<pk>[0-9]+)/$',views.SponsorDelete.as_view(), name='delete-sponsor'),

    #market/
   # url(r'^products$', views.ProductIndexView.as_view(), name = 'product-index'),
   # url(r'^products/(?P<pk>[0-9]+)/$', views.ProductDetailView.as_view(), name = 'product-detail'),

   # url(r'^products/add/$',views.ProductCreate.as_view(), name='add-product'),
   # url(r'^products/edit/(?P<pk>[0-9]+)/$',views.ProductUpdate.as_view(), name='edit-product'),
   # url(r'^products/delete/(?P<pk>[0-9]+)/$',views.ProductDelete.as_view(), name='delete-product'),

]
