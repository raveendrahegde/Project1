from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.template import Context, RequestContext
# Create your views here.

def doLogin(request):
	context = RequestContext(request, {'site_name': settings.SITE_NAME})
	return render(context, "firstapp/homepage.html")

def doLogout(request):
	print "CCC"
	context = RequestContext(request, {'site_name': settings.SITE_NAME})
	return render(context, "firstapp/loginpage.html")