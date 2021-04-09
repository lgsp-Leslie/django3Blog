#!/usr/bin/env python3
# coding=utf-8
# Version:python3.9
# Project:django3Blog
# File:views.py
# Data:2021/2/25 22:08
# Author:LGSP_Harold

from django.contrib.contenttypes.models import ContentType
# from django.core.cache import cache
from django.shortcuts import render

from access_statistics.utils import get_seven_days_read_data, get_days_hot_data, cache_hot_data
from blog.models import Blog


def home(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)

    dates, read_nums = get_seven_days_read_data(blog_content_type)

    today_hot_data = get_days_hot_data(blog_content_type, 0)
    yesterday_hot_data = get_days_hot_data(blog_content_type, 1)
    one_week_hot_data = get_days_hot_data(Blog, 7)
    one_month_hot_data = get_days_hot_data(Blog, 30)
    one_year_hot_data = get_days_hot_data(Blog, 365)

    # # 缓存热门排行数据
    # cache_one_week_hot_data = cache.get('cache_one_week_hot_data')
    # if cache_one_week_hot_data is None:
    #     cache.set('cache_one_week_hot_data', one_week_hot_data, 5)
    #     print('11')
    # else:
    #     print('22')

    cache_seven_days_read_data = cache_hot_data('seven_days_read_data', (dates, read_nums, ))

    cache_today_hot_data = cache_hot_data('today_hot_data', today_hot_data)
    cache_yesterday_hot_data = cache_hot_data('yesterday_hot_data', yesterday_hot_data)
    cache_one_week_hot_data = cache_hot_data('one_week_hot_data', one_week_hot_data)
    cache_one_month_hot_data = cache_hot_data('one_month_hot_data', one_month_hot_data)
    cache_one_year_hot_data = cache_hot_data('one_year_hot_data', one_year_hot_data)

    context = {
        'dates': cache_seven_days_read_data[0],
        'read_nums': cache_seven_days_read_data[1],
        'today_hot_data': cache_today_hot_data,
        'yesterday_hot_data': cache_yesterday_hot_data,
        'one_week_hot_data': cache_one_week_hot_data,
        'one_month_hot_data': cache_one_month_hot_data,
        'one_year_hot_data': cache_one_year_hot_data,
    }
    return render(request, 'home.html', context)
