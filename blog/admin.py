from django.contrib import admin

# from blog.models import Blog, BlogType, ReadNum
from blog.models import Blog, BlogType


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
    list_per_page = 9


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'blog_type', 'author', 'get_read_num', 'created_time', 'updated_time')
    list_per_page = 9


"""
@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'blog')
    list_per_page = 9
"""
