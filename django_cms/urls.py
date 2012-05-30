from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', 'django_cms.search.views.search'),
    url(r'^weblog/', include('django_blog.urls')),
    url(r'', include('django.contrib.flatpages.urls')),
)
