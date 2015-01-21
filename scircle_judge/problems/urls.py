from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'problems.views.list'),
    url(r'^(\d+)/$', 'problems.views.detail'),

)