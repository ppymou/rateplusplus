from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

from default import views 

urlpatterns = patterns('',
    url(r'^search/$', views.SearchPage), 
    url(r'^$', views.DefaultPage)
)
