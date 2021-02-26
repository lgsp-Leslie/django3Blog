#!/usr/bin/env python3
# coding=utf-8
# Version:python3.6.1
# Project:django3Blog
# File:views.py
# Data:2021/2/25 22:08
# Author:LGSP_Harold
from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'home.html', context)
