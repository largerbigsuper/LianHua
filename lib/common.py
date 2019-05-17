#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 下午2:30
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : common.py
from django.contrib.auth import login, logout

from LianHua.lianhua_settings import UID, CID


def customer_login(request, user):
    login(request, user)
    request.session[UID] = user.id
    request.session[CID] = user.customer.id


def admin_login(request, user):
    login(request, user)
    request.session[UID] = user.id


def common_logout(request):
    logout(request)
