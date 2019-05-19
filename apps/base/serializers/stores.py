#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 下午11:58
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : tags.py
from rest_framework import serializers

from datamodels.stores.models import Tag, mm_Tag, Store


class BaseTagIdSerialzier(serializers.Serializer):

    tag_id = serializers.PrimaryKeyRelatedField(queryset=mm_Tag.all())


class BaseStoreTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')


class BaseStoreSerializer(serializers.ModelSerializer):
    tags = BaseStoreTagSerializer(many=True, read_only=True)
    images = serializers.ListField()

    class Meta:
        model = Store
        fields = ('id', 'name', 'logo', 'desc', 'tel', 'wechat', 'address_info', 'images', 'tags', 'create_at')


