#about views
from django.shortcuts import render

# Create your views here.
#def constitution(request):
#	context = {} 
#	template = "constitution.html" 
#	return render(request, template, context)


def constitution(request):
	context = {} 
	template = "const.html" 
	return render(request, template, context)
