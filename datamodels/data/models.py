from datetime import datetime

from django.db import models

from LianHua.settings import DB_PREFIX
from lib.modelmanager import ModelManager


class ProductViewCountRecordManager(ModelManager):

    def add_count(self, product_id, amount=1):
        record, _ = self.get_or_create(product_id=product_id, date=datetime.today())
        record.total += amount
        record.save()


class ProductViewCountRecord(models.Model):
    """产品访问次数记录"""

    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True, unique_for_date=True, verbose_name='记录时间')
    total = models.IntegerField(default=0, verbose_name='访问次数')

    objects = ProductViewCountRecordManager()

    class Meta:
        db_table = DB_PREFIX + 'product_view_count_records'
        unique_together = [
            ['product', 'date']
        ]


class StoreViewCountRecordManager(ModelManager):

    def add_count(self, store_id, amount=1):
        record, _ = self.get_or_create(store_id=store_id, date=datetime.today())
        record.total += amount
        record.save()


class StoreViewCountRecord(models.Model):
    """店铺访问次数记录"""

    store = models.ForeignKey('stores.Store', on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now_add=True, unique_for_date=True, verbose_name='记录时间')
    total = models.IntegerField(default=0, verbose_name='访问次数')

    objects = StoreViewCountRecordManager()

    class Meta:
        db_table = 'store_view_count_records'
        unique_together = [
            ['store', 'date']
        ]


class CustomerAccessStoreRecordManager(ModelManager):

    def add_record(self, customer_id, store_id):
        self.create(customer_id=customer_id, store_id=store_id)


class CustomerAccessStoreRecord(models.Model):
    """用户访问店铺记录"""

    customer = models.ForeignKey('customers.Customer', on_delete=models.DO_NOTHING)
    store = models.ForeignKey('stores.Store', on_delete=models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add=True)

    objects = CustomerAccessStoreRecordManager()

    class Meta:
        db_table = DB_PREFIX + 'customer_access_store_records'


class CustomerAccessProductRecordManager(ModelManager):

    def add_record(self, customer_id, product_id):
        self.create(customer_id=customer_id, product_id=product_id)


class CustomerAccessProductRecord(models.Model):
    """用户访问产品记录"""

    customer = models.ForeignKey('customers.Customer', on_delete=models.DO_NOTHING)
    product = models.ForeignKey('products.Product', on_delete=models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add=True)

    objects = CustomerAccessProductRecordManager()

    class Meta:
        db_table = DB_PREFIX + 'customer_access_product_records'


class CustomerAccessVideoRecordManager(ModelManager):

    def add_record(self, customer_id, video_id):
        self.create(customer_id=customer_id, video_id=video_id)


class CustomerAccessVideoRecord(models.Model):
    """用户访问视频记录"""

    customer = models.ForeignKey('customers.Customer', on_delete=models.DO_NOTHING)
    video = models.ForeignKey('videos.Video', on_delete=models.DO_NOTHING)
    create_at = models.DateTimeField(auto_now_add=True)

    objects  = CustomerAccessVideoRecordManager()

    class Meta:
        db_table = DB_PREFIX + 'customer_access_video_records'


mm_ProductViewCountRecord = ProductViewCountRecord.objects
mm_StoreViewCountRecord = StoreViewCountRecord.objects
mm_CustomerAccessProductRecord = CustomerAccessProductRecord.objects
mm_CustomerAccessStoreRecord = CustomerAccessStoreRecord.objects
mm_CustomerAccessVideoRecord = CustomerAccessVideoRecord.objects


