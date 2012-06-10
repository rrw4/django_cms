from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', 'django_cms.search.views.search'),
    url(r'^weblog/categories/', include('django_blog.urls.categories')),
    url(r'^weblog/links/', include('django_blog.urls.links')),
    url(r'^weblog/tags/', include('django_blog.urls.tags')),
    url(r'^weblog/', include('django_blog.urls.entries')),
    url(r'', include('django.contrib.flatpages.urls')),
)
