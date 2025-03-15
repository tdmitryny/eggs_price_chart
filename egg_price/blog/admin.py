from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'published_date')
    list_filter = ('published_date',)
    search_fields = ('title', 'content')
    date_hierarchy = 'published_date'
