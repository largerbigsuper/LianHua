#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 下午10:27
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : router.py
from rest_framework import routers

from apps.customers.customers.viewsets import CustomerViewSet
from apps.customers.index.viewsets import ADViewSet
from apps.customers.products.viewsets import ProductViewSet, ProductTypeViewSet
from apps.customers.stores.viewsets import TagViewSet, StoreViewSet

customer_router = routers.DefaultRouter()

customer_router.register('u', CustomerViewSet, base_name='customer')
customer_router.register('tag', TagViewSet, base_name='customer-tag')
customer_router.register('store', StoreViewSet, base_name='customer-store')
customer_router.register('producttype', ProductTypeViewSet, base_name='customer-producttype')
customer_router.register('product', ProductViewSet, base_name='customer-product')
customer_router.register('ad', ADViewSet, base_name='customer-ad')
