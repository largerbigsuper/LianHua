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


class ModelManager(Manager, Const):
    pass

