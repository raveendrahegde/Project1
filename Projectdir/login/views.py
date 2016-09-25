from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from datetime import datetime
import json

from models import Users

def loginpage(request):
	return render_to_response("login/loginpage.html", {'site_name': settings.SITE_NAME}, context_instance=RequestContext(request))

def doLogin(request):
	data = request.GET
	email = data.get("inputEmail")
	password = data.get("inputPass")

	try:
		user = Users.objects.get(email=email)
		if password == user.password:
			user.isLoggedIn = True
			user.lastLogin = datetime.utcnow()
			user.save()
			request.session['email'] = email
			request.session['user_id'] = user.id
			return HttpResponseRedirect("/home")
		else:
			return HttpResponse("Sorry brother")
	except Exception as e:
		print "Error " + str(e)
		return HttpResponse("Can't find you")

def doLogout(request):
	user = Users.objects.get(email=request.session['email'])
	user.isLoggedIn = False
	user.save()
	return render_to_response("login/loginpage.html", {'site_name': settings.SITE_NAME}, context_instance=RequestContext(request))