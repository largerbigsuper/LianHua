#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 下午10:24
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : router.py
from rest_framework import routers

from apps.admin.admin.viewsets import AdminViewSet
from apps.admin.products.viewsets import ProductTypeViewSet, ProductViewSet
from apps.admin.stores.viewsets import StoreViewSet, TagViewSet

admin_router = routers.DefaultRouter()

admin_router.register('admin', AdminViewSet, base_name='admin-admin')
admin_router.register('tag', TagViewSet, base_name='admin-tag')
admin_router.register('store', StoreViewSet, base_name='admin-store')
admin_router.register('producttype', ProductTypeViewSet, base_name='admin-producttype')
admin_router.register('product', ProductViewSet, base_name='admin-product')

