#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 下午11:12
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : filters.py
from django_filters import rest_framework as filters

from datamodels.index.models import Ad


class AdFilter(filters.FilterSet):

    class Meta:
        model = Ad
        fields = {
            'name': ['icontains'],
            'status': ['exact'],
            'ad_type': ['exact'],
            'begin_at': ['lt', 'gt'],
            'end_at': ['lt', 'gt'],
        }

