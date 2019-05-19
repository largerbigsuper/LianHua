from django.db import models
from django_extensions.db.fields.json import JSONField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from LianHua.settings import DB_PREFIX
from lib.modelmanager import ModelManager


class ProductTypeManager(ModelManager):
    pass


class ProductType(MPTTModel):

    name = models.CharField(max_length=40, unique=True, db_index=True, verbose_name='类型')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    objects = ProductTypeManager()

    class Meta:
        db_table = DB_PREFIX + 'product_type'

    def __str__(self):
        return self.name


class ProductManager(ModelManager):

    def products_in_market(self):
        """可供销售的商品"""
        return self.filter(status=self.STATUS_ON_SAELF)


class Product(models.Model):

    store = models.ForeignKey('stores.Store', on_delete=models.CASCADE, verbose_name='店铺')
    name = models.CharField(max_length=200, verbose_name='产品名称', db_index=True)
    types = models.ManyToManyField('ProductType', blank=True)
    price = models.FloatField(default=0, verbose_name='价格')
    unit = models.CharField(max_length=100, verbose_name='计价单位')
    images = JSONField(max_length=1000, default='[]', verbose_name='图片')
    detail = models.CharField(max_length=10000, blank=True, verbose_name='详情')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    status = models.PositiveSmallIntegerField(choices=ProductManager.STATUS_CHOICE,
                                              default=ProductManager.STATUS_OFF_SHELF, verbose_name='上/下架')
    view_total = models.IntegerField(default=0, verbose_name='浏览总量')

    objects = ProductManager()

    class Meta:
        db_table = DB_PREFIX + 'products'

    def __str__(self):
        return self.name


mm_ProductType = ProductType.objects
mm_Product = Product.objects
