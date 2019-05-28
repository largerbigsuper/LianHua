#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 下午11:02
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : viewsets.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from apps.admin.stores.serializers import StoreSerializer
from apps.admin.stores.filters import AdminStoreFilter
from apps.base.serializers.stores import BaseStoreTagSerializer, BaseTagIdSerialzier
from datamodels.stores.models import mm_Store, mm_Tag


class TagViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = mm_Tag.all()
    serializer_class = BaseStoreTagSerializer


class StoreViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = mm_Store.all()
    serializer_class = StoreSerializer
    filter_class = AdminStoreFilter

    @action(methods=['post'], detail=True, serializer_class=BaseTagIdSerialzier)
    def add_tag(self, request, pk=None):
        store = self.get_object()
        serializer = BaseTagIdSerialzier(data=request.data)
        if serializer.is_valid():
            tag = serializer.validated_data['tag_id']
            if tag:
                store.tags.add(tag)
                return Response()
            else:
                return Response({'detail': '标签不存在'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], serializer_class=BaseTagIdSerialzier)
    def delete_tag(self, request, pk):
        store = self.get_object()
        serializer = BaseTagIdSerialzier(data=request.data)
        if serializer.is_valid():
            tag = serializer.validated_data['tag_id']
            if tag:
                store.tags.remove(tag)
                return Response()
            else:
                return Response(data={'detail': '标签不存在'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
