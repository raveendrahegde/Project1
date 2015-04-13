from django.conf.urls import patterns, url

from firstapp import views

urlpatterns = patterns('',
    url(r'^todo$', views.whatToDo),
    url(r'^nottodo$', views.notToDo)

)