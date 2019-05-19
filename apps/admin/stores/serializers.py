#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 下午11:02
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : serializers.py
from apps.base.serializers.stores import BaseStoreSerializer
from datamodels.stores.models import Store


class StoreSerializer(BaseStoreSerializer):

    class Meta:
        model = Store
        fields = ('id', 'name', 'logo', 'desc', 'tel', 'wechat', 'address_info', 'images', 'tags', 'create_at')
