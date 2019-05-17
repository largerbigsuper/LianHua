#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 下午9:53
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : viewsets.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from apps.admin.index.filters import AdFilter
from apps.admin.index.serializers import AdSerializer
from datamodels.index.models import mm_Ad


class AdminAdViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = AdSerializer
    queryset = mm_Ad.all()
    filter_class = AdFilter

