from django.conf.urls import patterns, url

from login import views

urlpatterns = patterns('',
    url(r'^login$', views.doLogin),
    url(r'^logout$', views.doLogout)

)