from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.views import logout

from default import views 

urlpatterns = patterns('',
    url(r'^feedback$', views.FeedbackHandler),
    url(r'^advertise$', views.AdHandler),
    url(r'^entity/(?P<pk>[0-9]+)/?$', views.EntityHandler),
    url(r'^entity/new/?$', views.NewEntityHandler),
    url(r'^graph$', views.GraphHandler),
    url(r'^profile$', views.ProfileHandler),

    url(r'^signup$', views.SignupHandler, name="signout-page"),
    url(r'^signin$', views.SigninHandler, name="signin-page"),
    url(r'^signout$', logout, {'next_page': '/signin'}),
    url(r'^privacy$', views.PrivacyHandler),
    url(r'^$', views.PageHandler)
)
