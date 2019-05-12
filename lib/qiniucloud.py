#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/6 下午7:35
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : qiniucloud.py
from qiniu import Auth
from LianHua.settings import QiNiuSettings


class QiniuServe:
    # 构建鉴权对象
    access_key = QiNiuSettings.ACCESS_KEY
    secret_key = QiNiuSettings.SECRET_KEY
    qiniuAuth = Auth(access_key, secret_key)
    bucket_name_dict = QiNiuSettings.BUCKET_NAME_DICT
    bucket_domain_dict = QiNiuSettings.BUCKET_DOMAIN_DICT

    @classmethod
    def get_bucket_name(cls, file_type):
        return cls.bucket_name_dict[file_type]

    @classmethod
    def gen_app_upload_token(cls, bucket_name):
        """
        app 上传token生成
        :param bucket_name: 文件存储空间名
        :param filename: 上传到七牛后保存的文件名
        :param user_id: 用户user_id
        :return:
        """
        # 上传策略示例
        # https://developer.qiniu.com/kodo/manual/1206/put-policy
        # policy = {
        #  # 'callbackUrl':'https://requestb.in/1c7q2d31',
        #  # 'callbackBody':'filename=$(fname)&filesize=$(fsize)'
        #  # 'persistentOps':'imageView2/1/w/200/h/200'
        #     'saveKey': '%s/$(etag)$(ext)' % user_id
        #  }
        policy = {
            # 'saveKey': '%s/$(etag)$(ext)' % user_id,
            'fsizeLimit': 10 * 1024 * 1024
        }
        #3600为token过期时间，秒为单位。3600等于一小时
        token = cls.qiniuAuth.upload_token(bucket_name, None, 3600, policy)
        return token
