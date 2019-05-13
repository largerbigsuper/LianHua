#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 下午7:53
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : viewsets.py
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.admin.admin.serializers import AdminUserSerializer, AdminLoginSerializer
from lib.common import admin_login, common_logout


class AdminViewSet(viewsets.ModelViewSet):

    permission_classes = []
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer

    @action(detail=False, methods=['post'], serializer_class=AdminLoginSerializer)
    def login(self, request):
        """登录"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.validated_data['account']
        password = serializer.validated_data['password']
        user = User.objects.filter(username=account).first()
        if user:
            user = authenticate(request, username=account, password=password)
            if user:
                admin_login(request, user)
                serailizer = AdminUserSerializer(user)
                return Response(data=serailizer.data)
            else:
                return Response(data={'detail': '账号或密码错误'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(data={'detail': '账号不存在'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def logout(self, request):
        """退登"""
        common_logout(request)
        return Response()
