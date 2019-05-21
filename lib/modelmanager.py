#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 上午12:52
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : modelmanager.py
from django.db.models import Manager


class Const(object):

    # product model
    STATUS_OFF_SHELF = 0
    STATUS_ON_SAELF = 1
    STATUS_CHOICE = (
        (STATUS_OFF_SHELF, '已下架'),
        (STATUS_ON_SAELF, '已上架'),
    )

    AD_STATUS_OFF = 0
    AD_STATUS_ON = 1
    AD_STATUS_CHOICE = (
        (AD_STATUS_OFF, '关闭'),
        (AD_STATUS_ON, '开启')
    )

    AD_TYPE_WEB = 0
    AD_TYPE_STORE = 1
    AD_TYPE_PRODUCT = 2
    AD_TYPE_PINCHE = 4
    AD_TYPE_CHOICE = (
        (AD_TYPE_WEB, '网页'),
        (AD_TYPE_STORE, '店铺'),
        (AD_TYPE_PRODUCT, '产品'),
        (AD_TYPE_PINCHE, '拼车'),
    )

    CAR_SERVICE_TYPE_1 = 1
    CAR_SERVICE_TYPE_2 = 2
    CAR_SERVICE_TYPE_3 = 3
    CAR_SERVICE_TYPE_4 = 4

    CAR_SERVICE_TYPE_CHOICE = (
        (CAR_SERVICE_TYPE_1, '车找人'),
        (CAR_SERVICE_TYPE_2, '人找车'),
        (CAR_SERVICE_TYPE_3, '货找车'),
        (CAR_SERVICE_TYPE_4, '车找货'),
    )

class ModelManager(Manager, Const):
    pass

