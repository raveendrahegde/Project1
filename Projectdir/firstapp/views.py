from django.shortcuts import render
from django.http import HttpResponse
from models import ThingsToDo, ThingsNotToDo

def home(request):	
	return render(request, "firstapp/loginpage.html")

def whatToDo(request):
	toDo=ThingsToDo.objects.all()
	context = {'todolist': toDo}
	return render(request,"firstapp/first.html",context)

def notToDo(request):
	notToDo=ThingsNotToDo.objects.all()
	context = {'notdolist': notToDo}
	return render(request,"firstapp/second.html",context)