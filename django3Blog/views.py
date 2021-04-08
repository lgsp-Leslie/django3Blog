#!/usr/bin/env python3
# coding=utf-8
# Version:python3.9
# Project:django3Blog
# File:views.py
# Data:2021/2/25 22:08
# Author:LGSP_Harold
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render

from access_statistics.utils import get_seven_days_read_data
from blog.models import Blog


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)

    context = {
        'dates': dates,
        'read_nums': read_nums,
    }
    return render(request, 'home.html', context)
