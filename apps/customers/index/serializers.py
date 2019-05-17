#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 上午12:20
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : serializers.py
from rest_framework import serializers

from datamodels.index.models import Ad


class ADSerailziers(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ('id', 'name', 'image', 'ad_type', 'resource_str')