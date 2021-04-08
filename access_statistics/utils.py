#!/usr/bin/env python3
# coding=utf-8
# Version:python3.9
# Project:django3Blog
# File:utils.py
# Data:2021/4/8 17:40
# Author:LGSP_Harold
from django.contrib.contenttypes.models import ContentType

from access_statistics.models import ReadNum


def read_statistics_once_read(request, obj):
    ct = ContentType.objects.get_for_model(obj)
    key = '%s_%s_read_num' % (ct.model, obj.pk)

    if not request.COOKIES.get(key):
        if ReadNum.objects.filter(content_type=ct, object_id=obj.id):
            # 存在对应记录
            readnum = ReadNum.objects.get(content_type=ct, object_id=obj.id)
        else:
            # 不存在对应记录
            readnum = ReadNum(content_type=ct, object_id=obj.id)
        # 计数+1
        readnum.read_num += 1
        readnum.save()
    return key
