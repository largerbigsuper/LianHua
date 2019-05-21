#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 下午10:46
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : customers.py
from rest_framework import serializers

from datamodels.customers.models import Customer


class BaseCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id', 'name', 'gender', 'avatar_url')

