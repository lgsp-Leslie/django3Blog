#!/usr/bin/env python3
# coding=utf-8
# Version:python3.9
# Project:django3Blog
# File:utils.py
# Data:2021/4/8 17:40
# Author:LGSP_Harold
import datetime

from django.contrib.contenttypes.models import ContentType
from django.db.models import Sum
from django.utils import timezone

from access_statistics.models import ReadNum, ReadDetail


def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = '%s_%s_read_num' % (ct.model, obj.pk)

    if not request.COOKIES.get(key):
        # 总阅读数+1
        # if ReadNum.objects.filter(content_type=ct, object_id=obj.pk):
        #     # 存在对应记录
        #     readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)
        # else:
        #     # 不存在对应记录
        #     readnum = ReadNum(content_type=ct, object_id=obj.pk)
        readnum, create = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
        readnum.read_num += 1
        readnum.save()

        # 当天阅读数+1
        date = timezone.now().date()
        # if ReadDetail.objects.filter(content_type=ct, object_id=obj.pk, date=date):
        #     read_detail = ReadDetail.objects.get(content_type=ct, object_id=obj.pk, date=date)
        # else:
        #     read_detail = ReadDetail(content_type=ct, object_id=obj.pk, date=date)
        read_detail, create = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)
        read_detail.read_num += 1
        read_detail.save()
    return key


# 过去七天阅读量
def get_seven_days_read_data(content_type):
    today = timezone.now().date()

    dates = []
    read_nums = []
    for i in range(7, 0, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_details = ReadDetail.objects.filter(content_type=content_type, date=date)
        result = read_details.aggregate(read_num_sum=Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates, read_nums
