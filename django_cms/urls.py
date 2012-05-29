from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_cms.views.home', name='home'),
    # url(r'^django_cms/', include('django_cms.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve',
                     { 'document_root': '/Users/rogerwang/projects/django_cms/media/js/tinymce/jscripts/tiny_mce' }),
    url(r'^search/$', 'django_cms.search.views.search'),
    url(r'^weblog/$', 'django_blog.views.entries_index'),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'django_blog.views.entry_detail'), 
    url(r'', include('django.contrib.flatpages.urls')),
)
