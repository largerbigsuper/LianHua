#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 下午10:36
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : serializers.py
from rest_framework import serializers

from apps.base.serializers.customers import BaseCustomerSerializer
from datamodels.services.models import CarService


class MyCarServiceSerializer(serializers.ModelSerializer):
    """我的约车服务"""

    class Meta:
        model = CarService
        fields = ('id', 'car_service_type', 'area_from', 'area_from_text', 'area_to', 'area_to_text',
                  'place_pass', 'start_at', 'tel', 'site_count', 'mark', 'published',
                  'update_at', 'create_at', 'range_type')


class CarServiceSerializer(serializers.ModelSerializer):
    """约车列表"""

    customer = BaseCustomerSerializer()

    class Meta:
        model = CarService
        fields = ('id', 'customer', 'car_service_type', 'area_from', 'area_from_text', 'area_to', 'area_to_text',
                  'place_pass', 'start_at', 'tel', 'site_count', 'mark', 'published',
                  'update_at', 'create_at', 'range_type')
