#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 上午10:38
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : pagenagations.py
from collections import OrderedDict

from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('page_count', self.page.paginator.num_pages),
            ('results', data)
        ]))
