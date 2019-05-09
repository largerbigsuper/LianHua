#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 下午2:01
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : viewsets.py
from rest_framework import viewsets
from rest_framework.response import Response

from LianHua.settings import CID
from apps.base.serializers.products import BaseProductTypeSerializer
from apps.customers.products.serializers import ProductSerializer
from datamodels.data.models import mm_ProductViewCountRecord, mm_CustomerAccessProductRecord
from datamodels.products.models import mm_Product, mm_ProductType


class ProductTypeViewSet(viewsets.ReadOnlyModelViewSet):

    permission_classes = []
    serializer_class = BaseProductTypeSerializer
    queryset = mm_ProductType.all()


class ProductViewSet(viewsets.ReadOnlyModelViewSet):

    permission_classes = []
    serializer_class = ProductSerializer
    queryset = mm_Product.products_in_market()

    def retrieve(self, request, *args, **kwargs):
        product = self.get_object()
        serializer = self.get_serializer(product)
        if request.user.is_authenticated:
            # 记录访问记录
            mm_CustomerAccessProductRecord.add_record(request.session[CID], product.id)
            mm_ProductViewCountRecord.add_count(product.id)
            product.view_total += 1
            product.save()
        return Response(serializer.data)


