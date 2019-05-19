#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 上午1:34
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : serializers.py
from rest_framework import serializers

from apps.base.serializers.stores import BaseStoreSerializer
from apps.base.serializers.stores import BaseStoreTagSerializer
from datamodels.stores.models import Store


class StoreSerializer(BaseStoreSerializer):

    class Meta:
        model = Store
        fields = ('id', 'name', 'logo', 'desc', 'tel', 'wechat', 'address_info', 'images', 'tags', 'create_at')


class StoreSimpleSerializer(BaseStoreSerializer):

    class Meta:
        model = Store
        fields = ('id', 'name', 'logo')
