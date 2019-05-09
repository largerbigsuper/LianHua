#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 下午11:58
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : tags.py
from rest_framework import serializers

from datamodels.stores.models import Tag, mm_Tag


class BaseTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('id', 'name')


class BaseTagIdSerialzier(serializers.Serializer):

    tag_id = serializers.PrimaryKeyRelatedField(queryset=mm_Tag.all())
