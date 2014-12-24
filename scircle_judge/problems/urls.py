from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # API

    # problemlist
    url(r'^$', problems.views.index),

)