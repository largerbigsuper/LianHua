#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 上午10:58
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : serializers.py
from rest_framework import serializers

from apps.base.serializers.products import BaseProductTypeSerializer
from apps.customers.stores.serializers import StoreSimpleSerializer
from datamodels.products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    store = StoreSimpleSerializer()
    types = BaseProductTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'store', 'name', 'types', 'price', 'unit', 'images', 'detail',
                  'create_at', 'update_at', 'view_total')
