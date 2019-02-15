from django.shortcuts import render

# Create your views here.

def projectspage(request):
	context = {} 
	template = "projects.html" 
	return render(request, template, context)

def pyladies(request):
	context = {} 
	template = "pyladies.html" 
	return render(request, template, context)


def pykids(request):
	context = {} 
	template = "pykids.html" 
	return render(request, template, context)


def pydata(request):
	context = {} 
	template = "pydata.html" 
	return render(request, template, context)


def pyclub(request):
	context = {} 
	template = "pyclub.html" 
	return render(request, template, context)
