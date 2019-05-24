#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 下午1:27
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : viewsets.py
import requests
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from LianHua import settings
from apps.customers.customers.serilizers import CustomerProfileSerializer, MiniprogramLoginSerializer, LoginSerializer, \
    RegisterSerializer
from datamodels.customers.models import mm_Customer
from lib.common import customer_login, common_logout


class CustomerViewSet(viewsets.ModelViewSet):

    permission_classes = []
    serializer_class = CustomerProfileSerializer
    queryset = mm_Customer.all()

    @csrf_exempt
    @action(methods=['post'], detail=False, serializer_class=MiniprogramLoginSerializer, permission_classes=[])
    def login_miniprogram(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['code']
        wx_res = requests.get(settings.MinprogramSettings.LOGIN_URL + code)
        ret_json = wx_res.json()
        if 'openid' not in ret_json:
            return Response(data=ret_json, status=status.HTTP_400_BAD_REQUEST)
        openid = ret_json['openid']
        # session_key = ret_json['session_key']
        # unionid = ret_json.get('session_key')
        customer = mm_Customer.get_customer_by_miniprogram(openid)
        customer_login(request, customer.user)
        data = {
            'id': customer.id,
            'user_id': customer.user.id,
            'name': customer.name,
        }
        return Response(data=data)

    @csrf_exempt
    @action(detail=False, methods=['post'], serializer_class=LoginSerializer)
    def login(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.validated_data['account']
        password = serializer.validated_data['password']
        customer = mm_Customer.filter(account=account).first()
        if customer:
            user = authenticate(request, username=account, password=password)
            if user:
                customer_login(request, user)
                serailizer = CustomerProfileSerializer(customer)
                return Response(data=serailizer.data)
            else:
                return Response(data={'detail': '账号或密码错误'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'detail': '账号不存在'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], serializer_class=RegisterSerializer)
    def enroll(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.validated_data['account']
        password = serializer.validated_data['password']
        customer = mm_Customer.add(account=account, password=password)
        return Response(data={'account': account})

    @action(detail=False, methods=['get'])
    def logout(self, request):
        common_logout(request)
        return Response()

    @action(detail=False, methods=['get', 'post'], permission_classes=[IsAuthenticated])
    def profile(self, request):
        """个人信息"""
        if request.method == 'GET':
            serializer = self.serializer_class(request.user.customer)
            return Response(data=serializer.data)
        else:
            serializer = self.serializer_class(request.user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data)
            else:
                return Response(data=serializer.error, status=status.HTTP_400_BAD_REQUEST)

