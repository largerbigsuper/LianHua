#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 下午1:14
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : viewsets.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.common.area.serializers import AreaSerializer
from datamodels.common.models import mm_Area


class AreaViewSet(viewsets.ModelViewSet):
    serializer_class = AreaSerializer
    queryset = mm_Area.all().order_by('parent_id')

    @action(detail=False)
    def province(self, request):
        self.queryset = mm_Area.province()
        serializer = self.serializer_class(self.queryset, many=True)

        return Response(data=serializer.data)

    @action(detail=True)
    def citys(self, request, pk=None):
        self.queryset = mm_Area.citys_in_province(pk)
        serializer = self.serializer_class(self.queryset, many=True)

        return Response(data=serializer.data)

    @action(detail=True)
    def towns(self, request, pk=None):
        self.queryset = mm_Area.towns_in_city(pk)
        serializer = self.serializer_class(self.queryset, many=True)

        return Response(data=serializer.data)
