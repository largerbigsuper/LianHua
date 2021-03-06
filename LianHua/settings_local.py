#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 下午1:00
# @Author  : Frankie
# @Email   : zaihuazhao@163.com
# @File    : settings_local.py
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'NAME': 'lianhua_db',
        'PASSWORD': 'Password123/',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'OPTIONS': {
            'init_command': 'SET CHARACTER SET utf8mb4',
            'charset': 'utf8mb4',
        },
        'TEST': {
            'NAME': 'test_lianhua_db',
            'CHARSET': 'utf8mb4',
        }
    }
}


class MinprogramSettings:
    APP_ID = 'wx1743dc274cf46871'
    APP_SECRET = '648a7ae2cbf66aa7e48992d76f46e621'
    LOGIN_URL = 'https://api.weixin.qq.com/sns/jscode2session' \
                '?appid={}&secret={}&grant_type=authorization_code&js_code='.format(APP_ID, APP_SECRET)
