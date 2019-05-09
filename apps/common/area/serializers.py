#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 下午1:13
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : serializers.py
from rest_framework import serializers

from datamodels.common.models import Area


class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = ('id', 'code', 'name')


class CitySerializer(serializers.ModelSerializer):
    children = AreaSerializer(many=True)

    class Meta:
        model = Area
        fields = ('id', 'code', 'name', 'children')


class ProvinceSerializer(serializers.ModelSerializer):
    children = AreaSerializer(many=True)

    class Meta:
        model = Area
        fields = ('id', 'code', 'name', 'children')

