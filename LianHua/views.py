#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 上午12:00
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : views.py
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from lib.qiniucloud import QiniuServe


class UploadTokenView(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):

        file_type = request.query_params.get('file_type', 'image')
        if file_type not in ['image', 'video']:
            return Response({'detail': 'file_type错误'}, status=status.HTTP_400_BAD_REQUEST)
        bucket_name = QiniuServe.get_bucket_name(file_type)
        token = QiniuServe.gen_app_upload_token(bucket_name)
        data = {'token': token}

        return Response(data)
