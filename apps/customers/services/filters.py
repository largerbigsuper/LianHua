#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 下午11:19
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : filters.py
from django_filters import rest_framework as filters

from datamodels.services.models import CarService


class CarServiceFilter(filters.FilterSet):

    class Meta:
        model = CarService
        fields = {
            'car_service_type': ['exact'],
            'range_type': ['exact'],
            'area_from': ['exact'],
            'area_to': ['exact'],
            'area_from_text': ['contains'],
            'area_to_text': ['contains'],
            'start_at': ['lt', 'gt'],
            'site_count': ['lt', 'gt', 'exact'],
        }

