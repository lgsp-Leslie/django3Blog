from django.contrib import admin

from blog.models import Blog, BlogType


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
    list_per_page = 9


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog_type', 'author', 'created_time', 'updated_time')
    list_per_page = 9
