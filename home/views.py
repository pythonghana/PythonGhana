#home views
from django.shortcuts import render
from django.shortcuts import (
render_to_response
)
from django.template import RequestContext


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

def pykidsghana(request):
	context = {}
	template = "pykidsghana.html"
	return render(request, template, context)

def pyscholarsghana(request):
	context = {}
	template = "pyscholarsghana.html"
	return render(request, template, context)


def pyclubghana(request):
	context = {}
	template = "pyclubghana.html"
	return render(request, template, context)

def pydataghana(request):
	context = {}
	template = "pydataghana.html"
	return render(request, template, context)

def pyconghana(request):
	context = {}
	template = "pyconghana.html"
	return render(request, template, context)

def accra(request):
	context = {}
	template = "accra.html"
	return render(request, template, context)

def kumasi(request):
	context = {}
	template = "kumasi.html"
	return render(request, template, context)

def ho(request):
	context = {}
	template = "ho.html"
	return render(request, template, context)

def capecoast(request):
	context = {}
	template = "capecoast.html"
	return render(request, template, context)

# HTTP Error 400
def bad_request(request):
    response = render_to_response(
    '400.html',
    context_instance=RequestContext(request)
    )

    response.status_code = 400

    return response