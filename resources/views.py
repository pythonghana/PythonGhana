from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView
from django.template import RequestContext
from django.views.generic.detail import DetailView
from .models import Book, Video, Article, Link
from .forms import BookForm
from hitcount.views import HitCountDetailView


class Resources(ListView):
    context_object_name = 'resources'
    template_name = 'resourcesN.html'
    queryset = Book.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Resources, self).get_context_data(**kwargs)
        context['videos'] = Video.objects.all()
        context['articles'] = Article.objects.all()
        context['links'] = Link.objects.all()
        context['books'] = self.queryset
        return context

