#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 上午10:59
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : products.py
from rest_framework import serializers

from datamodels.products.models import ProductType, Product


class BaseProductTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductType
        fields = ('id', 'name')


class BaseProductSerializer(serializers.ModelSerializer):

    types = BaseProductTypeSerializer(many=True, read_only=True)
    images = serializers.ListField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'types', 'price', 'unit', 'images', 'detail',
                  'create_at', 'update_at', 'view_total')
