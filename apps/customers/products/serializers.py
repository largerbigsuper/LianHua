#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 上午10:58
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : serializers.py
from apps.base.serializers.products import BaseProductSerializer
from datamodels.products.models import Product


class ProductSerializer(BaseProductSerializer):

    class Meta:
        model = Product
        fields = ('id', 'store', 'name', 'types', 'price', 'unit', 'images', 'detail',
                  'create_at', 'update_at', 'view_total')
