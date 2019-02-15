#about views
from django.shortcuts import render

# Create your views here.

def aboutpage(request):
	context = {} 
	template = "about.html" 
	return render(request, template, context)