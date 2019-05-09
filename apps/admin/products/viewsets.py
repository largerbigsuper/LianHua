#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 上午2:32
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : viewsets.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from apps.admin.products.serializers import ProductSerializer, ProductTypeIdSerialzier
from apps.base.serializers.products import BaseProductTypeSerializer
from datamodels.products.models import mm_ProductType, mm_Product


class ProductTypeViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = mm_ProductType.all()
    serializer_class = BaseProductTypeSerializer


class ProductViewSet(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = mm_Product.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['post'], serializer_class=ProductTypeIdSerialzier)
    def add_producttype(self, request, pk=None):
        """增加类型标签"""
        product = self.get_object()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            producttype = serializer.validated_data['producttype_id']
            product.types.add(producttype)
            return Response()
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], serializer_class=ProductTypeIdSerialzier)
    def delete_producttype(self, request, pk=None):
        """删除标签"""
        product = self.get_object()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            producttype = serializer.validated_data['producttype_id']
            product.types.remove(producttype)
            return Response()
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def set_on_shelf(self, request, pk=None):
        """设置商品上架"""
        product = self.get_object()
        product.status = mm_Product.STATUS_ON_SAELF
        product.save()
        return Response()

    @action(detail=True, methods=['post'])
    def set_off_shelf(self, request, pk=None):
        """设置商品下架"""
        product = self.get_object()
        product.status = mm_Product.STATUS_OFF_SHELF
        product.save()
        return Response()

