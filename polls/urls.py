__author__ = 'Administrator'
from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    url(r'^json/$', views.json, name='json'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
)