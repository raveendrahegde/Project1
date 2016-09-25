from django.shortcuts import render
from django.http import HttpResponse
from models import ThingsToDo, ThingsNotToDo
from django.conf import settings
from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response

def home(request):
	try:
		'''
		#Long way
		context = RequestContext(request, {'site_name': settings.SITE_NAME})
		template = loader.get_template("firstapp/loginpage.html")
		rendered = template.render(context)
		return HttpResponse(rendered)'''

		#Short way
		return render_to_response("market/loginpage.html", {'site_name': settings.SITE_NAME}, context_instance=RequestContext(request))
	except Exception as e:
		print "Error rendering login template - ", str(e)


def whatToDo(request):
	toDo=ThingsToDo.objects.all()
	context = {'todolist': toDo}
	return render(request,"market/first.html",context)

def notToDo(request):
	notToDo=ThingsNotToDo.objects.all()
	context = {'notdolist': notToDo}
	return render(request,"market/second.html",context)