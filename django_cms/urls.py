from django.conf.urls import *
from django.contrib import admin
admin.autodiscover()

from django_blog.models import Entry

entry_info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'pub_date',
}

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', 'django_cms.search.views.search'),
    url(r'^weblog/$', 'django.views.generic.date_based.archive_index', entry_info_dict),
    url(r'^weblog/(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', entry_info_dict),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/$', 'django.views.generic.date_based.archive_month', entry_info_dict),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'django.views.generic.date_based.archive_day', entry_info_dict),
    url(r'^weblog/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'django.views.generic.date_based.object_detail', entry_info_dict), 
    url(r'', include('django.contrib.flatpages.urls')),
)
