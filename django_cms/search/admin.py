from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

from django_cms.search.models import SearchKeyword

class SearchKeywordAdmin(admin.ModelAdmin):
    pass

class SearchKeywordInline(admin.StackedInline):
    model = SearchKeyword

class FlatPageAdminWithKeywords(FlatPageAdmin):
    inlines = [SearchKeywordInline]

admin.site.register(SearchKeyword, SearchKeywordAdmin)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdminWithKeywords)


