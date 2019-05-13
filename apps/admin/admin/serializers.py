#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 下午7:52
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers


class AdminLoginSerializer(serializers.Serializer):

    account = serializers.CharField()
    password = serializers.CharField()


class AdminUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')

