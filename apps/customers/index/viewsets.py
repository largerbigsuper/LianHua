#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 上午12:20
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : viewsets.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.customers.index.serializers import ADSerailziers
from datamodels.index.models import mm_Ad


class ADViewSet(viewsets.ReadOnlyModelViewSet):

    permission_classes = []
    serializer_class = ADSerailziers
    queryset = mm_Ad.customer_ad_queryset()

    @action(detail=False)
    def homepage(self, request):
        """首页广告"""
        queryset = mm_Ad.index_ads()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
