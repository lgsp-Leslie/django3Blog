from django.contrib import admin

from access_statistics.models import ReadNum, ReadDetail


@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'read_num')


@admin.register(ReadDetail)
class ReadDetailAdmin(admin.ModelAdmin):
    list_display = ('date', 'content_object', 'read_num')
