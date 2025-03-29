from django.contrib import admin

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','description','date')
    list_display_links = ('title'),



admin.site.register(Article,ArticleAdmin)
# Register your models here.
