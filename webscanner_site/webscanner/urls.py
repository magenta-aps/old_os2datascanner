"""URL patterns."""

import django_xmlrpc.views
from django.conf import settings
from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Include webscanner URLs
    url(r'^', include('os2webscanner.urls')),
    # Enable admin
    url(r'^admin/', admin.site.urls),
    # XMLRPC
    url(r'^xmlrpc/$', django_xmlrpc.views.handle_xmlrpc, name='xmlrpc'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [url(r'^debug/', include(debug_toolbar.urls))]