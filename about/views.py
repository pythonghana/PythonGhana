#about views
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from about.models import About
# Create your views here.



def about(request):
	about = About.objects.all()
	context = {
        'about': about
    }
	template = "aboutN.html"
	return render(request, template, context)


def aboutpage(request):
	context = {} 
	template = "about.html" 
	return render(request, template, context)