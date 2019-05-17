#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 下午9:53
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : serializers.py
from rest_framework import serializers

from datamodels.index.models import Ad
from lib.exceptions import PramsException


class AdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ad
        fields = ('id', 'name', 'image', 'ad_type', 'resource_str', 'status', 'begin_at', 'end_at', 'create_at')

    def save(self, **kwargs):
        if self.validated_data['begin_at'] < self.validated_data['end_at']:
            raise PramsException('开始时间不能早于结束时间')
        return super().save(**kwargs)
