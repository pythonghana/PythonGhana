#home views
from django.shortcuts import render

# Create your views here.

def homepage(request):
	context = {} 
	template = "homepage.html" 
	return render(request, template, context)

def home(request):
	context = {} 
	template = "home1.html" 
	return render(request, template, context)

def resources(request):
	context = {} 
	template = "resources.html" 
	return render(request, template, context)

def resources(request):
	context = {} 
	template = "pyconghana.html" 
	return render(request, template, context)
