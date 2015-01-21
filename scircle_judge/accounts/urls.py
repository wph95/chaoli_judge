from django.conf.urls import patterns, include, url
urlpatterns = patterns('',
    # Accounts
    url(r'^login/', 'accounts.views.login'),
    url(r'^logout/', 'accounts.views.logout'),
)
