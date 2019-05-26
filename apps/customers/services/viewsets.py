#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 下午10:37
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : viewsets.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from LianHua.lianhua_settings import UID
from apps.customers.services.filters import CarServiceFilter
from apps.customers.services.serializers import CarServiceSerializer, MyCarServiceSerializer
from datamodels.services.models import mm_CarService


class CarServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """约车服务列表"""

    permission_classes = []
    serializer_class = CarServiceSerializer
    queryset = mm_CarService.all()
    filter_class = CarServiceFilter
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ['start_at', 'update_at']


class MyCarServiceViewSet(viewsets.ModelViewSet):
    """我的约车服务"""

    permission_classes = (IsAuthenticated, )
    serializer_class = MyCarServiceSerializer

    def get_queryset(self):
        return mm_CarService.mycarservice(self.request.user.customer.id)

    def perform_create(self, serializer):
        serializer.save(customer_id=self.request.user.customer.id)

