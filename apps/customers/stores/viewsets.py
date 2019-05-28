#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 上午1:24
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : viewsets.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from LianHua.lianhua_settings import CID
from apps.base.serializers.products import BaseProductSerializer
from apps.base.serializers.stores import BaseStoreTagSerializer
from apps.customers.stores.serializers import StoreSerializer
from apps.customers.stores.filters import StoreFilter
from datamodels.data.models import mm_CustomerAccessStoreRecord, mm_StoreViewCountRecord
from datamodels.products.models import mm_Product
from datamodels.stores.models import mm_Tag, mm_Store


class TagViewSet(viewsets.ReadOnlyModelViewSet):

    permission_classes = []
    queryset = mm_Tag.all()
    serializer_class = BaseStoreTagSerializer


class StoreViewSet(viewsets.ReadOnlyModelViewSet):

    permission_classes = []
    queryset = mm_Store.all()
    serializer_class = StoreSerializer
    filter_class = StoreFilter

    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        store = self.get_object()
        product_qs = mm_Product.filter(store=store)
        page = self.paginate_queryset(product_qs)
        serializer = BaseProductSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        store = self.get_object()
        serializer = self.get_serializer(store)
        if request.user.is_authenticated:
            # 记录访问记录
            if request.user.is_authenticated:
                mm_CustomerAccessStoreRecord.add_record(request.session[CID], store.id)
            mm_StoreViewCountRecord.add_count(store.id)
        return Response(serializer.data)


