#!/usr/bin/env python3
# coding=utf-8
# Version:python3.6.1
# Project:django3Blog
# File:urls.py
# Data:2021/2/25 13:01
# Author:LGSP_Harold
from django.urls import path

from blog import views

urlpatterns = [
    # path('', views.blog_list, name='blog_list'),
    path('<int:blog_pk>', views.blog_detail, name='blog_detail'),
    path('type/<int:blog_type_pk>', views.blogs_with_type, name='blogs_with_type')

]
