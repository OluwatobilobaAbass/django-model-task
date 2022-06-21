from django.contrib import admin
from .blog import Article

class ArticleDB(admin.ModelAdmin):
    list_display = [
    'title', 'body', 'author', 'created_date', 'published_date'
    ]