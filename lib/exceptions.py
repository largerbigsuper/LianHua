#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 下午2:01
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : exceptions.py
from rest_framework import status
from rest_framework.exceptions import APIException
from django.utils.translation import ugettext_lazy as _


class DBException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = _('数据异常')
    default_code = '数据异常'
