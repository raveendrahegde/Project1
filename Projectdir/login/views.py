from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def doLogin(request):
	return HttpResponse('You are logged in')

def doLogout(request):
	return HttpResponse('You are logged out')