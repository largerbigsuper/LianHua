#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 上午10:43
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : render.py
from rest_framework.renderers import JSONRenderer


class FormatedJSONRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context['response']
        status_code_str = str(response.status_code)
        if status_code_str.startswith('2'):
            response.status_code = 200
            if data:
                if 'msg' not in data:
                    data = {
                        'msg': 'OK',
                        'data': data
                    }
            else:
                data = {
                    'msg': 'OK',
                    'data': data
                }
        return super().render(data, accepted_media_type, renderer_context)
