#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 下午10:37
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : viewsets.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from apps.admin.services.serializers import AdminCarServiceSerializer
from apps.admin.services.filters import AdminCarServiceFilter
from datamodels.services.models import mm_CarService


class AdminCarServiceViewSet(viewsets.ModelViewSet):
    """约车服务列表"""

    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = AdminCarServiceSerializer
    queryset = mm_CarService.all()
    filter_class = AdminCarServiceFilter
