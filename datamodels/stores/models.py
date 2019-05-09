from django.db import models

from LianHua.settings import AUTH_USER_MODEL, DB_PREFIX
from lib.modelmanager import ModelManager


class TagManager(ModelManager):
    pass


class Tag(models.Model):

    name = models.CharField(max_length=10, unique=True, verbose_name='标签名')

    objects = TagManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = DB_PREFIX + 'tag'


class StoreManager(ModelManager):
    pass


class Store(models.Model):

    name = models.CharField(max_length=40, verbose_name='店名')
    logo = models.CharField(max_length=200, blank=True, verbose_name='店铺logo')
    owner = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    desc = models.CharField(max_length=400, blank=True, verbose_name='简介')
    tel = models.CharField(max_length=20, blank=True, verbose_name='电话')
    wechat = models.CharField(max_length=40, blank=True, verbose_name='微信')
    address_info = models.CharField(max_length=120, blank=True, verbose_name='地址信息')
    area = models.ForeignKey('common.Area', on_delete=models.CASCADE, null=True, blank=True)
    images = models.CharField(max_length=500, default='[]', verbose_name='店铺图片')
    tags = models.ManyToManyField('Tag', blank=True)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    objects = StoreManager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = DB_PREFIX + 'stores'


mm_Tag = Tag.objects
mm_Store = Store.objects
