from __future__ import unicode_literals

from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.i18n import set_language

from mezzanine.core.views import direct_to_template
from mezzanine.conf import settings


admin.autodiscover()

urlpatterns = i18n_patterns(
    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.
    url("^admin/", include(admin.site.urls)),
)

if settings.USE_MODELTRANSLATION:
    urlpatterns += [
        url('^i18n/$', set_language, name='set_language'),
    ]

urlpatterns += [

    url("^$", direct_to_template, {"template": "index.html"}, name="home"),
    #url('^faq/', include('faq.urls')),
    url(r'^events/', include('events.urls', namespace='calendar')),
    url(r'^home', direct_to_template, {"template": "home1.html"}, name="home"),
    url(r'^about/', include('about.urls')),
    url(r'^coc/', include('coc.urls')),
    url(r'^gallery/', include('app.urls')),
    url(r'^constitution/', include('constitution.urls')),
   # url(r'projects/', include('projects.urls')),
    url(r'^resources', direct_to_template, {"template": "resources.html"}, name="resources"),
     url(r'^pyconghana', direct_to_template, {"template": "pyconghana.html"}, name="pyconghana"),

    url("^", include("mezzanine.urls")),
]

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"