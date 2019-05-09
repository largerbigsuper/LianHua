#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 下午1:27
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : serilizers.py
from rest_framework import serializers

from datamodels.customers.models import Customer

Profile_Fields = ('id', 'user_id', 'account', 'mini_openid', 'name', 'age', 'gender', 'avatar_url', 'create_at')


class MiniprogramLoginSerializer(serializers.Serializer):

    code = serializers.CharField()


class RegisterSerializer(serializers.Serializer):

    account = serializers.CharField()
    password = serializers.CharField()


class LoginSerializer(serializers.Serializer):

    account = serializers.CharField()
    password = serializers.CharField()


class CustomerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = Profile_Fields
        read_only_fields = ('user_id', 'account', 'mini_openid')
