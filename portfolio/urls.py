from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^resume/', include('resume.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.MEDIA_ROOT})
)
