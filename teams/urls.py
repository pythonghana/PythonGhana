from django.conf.urls import include, url
from . import views
from .views import *

urlpatterns = [
    url(r'^$', TeamListView.as_view(), name='team_list'),
    url(r'^/<slug:slug>/', TeamDetailView.as_view(), name='team_detail'),
    url(r'^/new/', views.team_new, name='team_new'),
    url(r'^/<slug:slug>/edit/', views.team_edit, name='team_edit'),
    url(r'^hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),   
]


