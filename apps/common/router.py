#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 下午10:26
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : router.py
from rest_framework import routers

from apps.common.area.viewsets import AreaViewSet

common_router = routers.DefaultRouter()

common_router.register('area', AreaViewSet, base_name='area')

