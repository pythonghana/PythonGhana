from django.shortcuts import render

# Create your views here.


def cocpage(request):
	context = {} 
	template = "cocN.html" 
	return render(request, template, context)
