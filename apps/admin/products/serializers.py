#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 上午2:28
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : serializers.py
from rest_framework import serializers

from apps.base.serializers.products import BaseProductSerializer
from datamodels.products.models import Product, mm_ProductType


class ProductTypeIdSerialzier(serializers.Serializer):

    producttype_id = serializers.PrimaryKeyRelatedField(queryset=mm_ProductType.all())


class ProductSerializer(BaseProductSerializer):

    class Meta:
        model = Product
        fields = ('id', 'store', 'name', 'types', 'price', 'unit', 'images', 'detail',
                  'create_at', 'update_at', 'status', 'view_total')
        read_only_fields = ('view_total',)
