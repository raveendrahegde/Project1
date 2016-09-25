from django.conf.urls import patterns, url

from login import views

urlpatterns = patterns('',
    url(r'^$', views.loginpage),
    url(r'^login$', views.loginpage),
    url(r'^dologin$', views.doLogin),
    url(r'^logout$', views.doLogout)

)