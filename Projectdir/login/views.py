from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def doLogin(request):
	return render(request, "firstapp/homepage.html")

def doLogout(request):
	return render(request, "firstapp/loginpage.html")