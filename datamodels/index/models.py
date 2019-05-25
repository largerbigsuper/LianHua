from datetime import datetime

from django.db import models

from LianHua.lianhua_settings import DB_PREFIX
from lib.modelmanager import ModelManager


class AdManager(ModelManager):

    # 首页显示几个
    Index_AD_Count = 4

    def index_ads(self):
        """返回首页广告"""
        return self.filter(status=self.AD_STATUS_ON).order_by('-begin_at')[:self.Index_AD_Count]

    def customer_ad_queryset(self):
        """普通用户能查看的广告"""
        return self.filter(status=self.AD_STATUS_ON).order_by('-begin_at')


class Ad(models.Model):

    name = models.CharField(max_length=100, verbose_name='名称')
    image = models.CharField(max_length=200, verbose_name='封面图')
    ad_type = models.PositiveSmallIntegerField(choices=AdManager.AD_TYPE_CHOICE,
                                               default=AdManager.AD_TYPE_WEB,
                                               verbose_name='类型')
    resource_str = models.CharField(max_length=200, verbose_name='资源id(str)')
    status = models.PositiveSmallIntegerField(choices=AdManager.AD_STATUS_CHOICE,
                                              default=AdManager.AD_STATUS_OFF,
                                              verbose_name='关闭|开启')
    begin_at = models.DateTimeField(verbose_name='首页显示开始时间', blank=True)
    end_at = models.DateTimeField(verbose_name='首页显示结束时间', blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    objects = AdManager()

    class Meta:
        db_table = DB_PREFIX + 'ads'
        ordering = ['status', '-begin_at']

    def __str__(self):
        return self.name


mm_Ad = Ad.objects
