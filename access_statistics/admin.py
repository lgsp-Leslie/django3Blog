from django.contrib import admin

from access_statistics.models import ReadNum


@admin.register(ReadNum)
class ReadNumAdmin(admin.ModelAdmin):
    list_display = ('content_object', 'read_num')
