#resources url

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *

urlpatterns = [
    url(r'^$', Resources.as_view(), name='books'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

