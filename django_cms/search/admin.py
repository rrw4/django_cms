from django.contrib import admin

from django_cms.search.models import SearchKeyword

class SearchKeywordAdmin(admin.ModelAdmin):
    pass

admin.site.register(SearchKeyword, SearchKeywordAdmin)



