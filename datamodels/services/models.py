from django.db import models

from LianHua.lianhua_settings import DB_PREFIX
from lib.modelmanager import ModelManager


class CarServiceManager(ModelManager):

    def mycarservice(self, customer_id):
        return self.filter(customer_id=customer_id)


class CarService(models.Model):
    """约车服务"""

    car_service_type = models.PositiveSmallIntegerField(choices=ModelManager.CAR_SERVICE_TYPE_CHOICE,
                                                        default=ModelManager.CAR_SERVICE_TYPE_1,
                                                        verbose_name='服务类型')
    range_type = models.PositiveSmallIntegerField(choices=ModelManager.CAR_RANGE_CHOICE,
                                                  default=ModelManager.CAR_RANGE_XIANNEI,
                                                  verbose_name='范围')
    customer = models.ForeignKey(
        'customers.Customer', on_delete=models.CASCADE, verbose_name='发布人')
    area_from = models.ForeignKey('common.Area', on_delete=models.DO_NOTHING, related_name='area_from',
                                  null=True, blank=True, verbose_name='出发地')
    area_from_text = models.CharField(max_length=200, verbose_name='出发地详情')
    area_to = models.ForeignKey('common.Area', on_delete=models.DO_NOTHING, related_name='area_to',
                                null=True, blank=True, verbose_name='目的地')
    area_to_text = models.CharField(max_length=200, verbose_name='目的地详情')
    place_pass = models.CharField(
        max_length=200, blank=True, verbose_name='途径地点')
    start_at = models.DateTimeField(verbose_name='出发时间')
    tel = models.CharField(max_length=20, verbose_name='联系方式')
    site_count = models.PositiveSmallIntegerField(
        default=0, verbose_name='座位个数')
    mark = models.CharField(max_length=500, blank=True, verbose_name='备注')
    published = models.BooleanField(default=False, verbose_name='已发布|未发布')
    update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    objects = CarServiceManager()

    class Meta:
        db_table = DB_PREFIX + 'car_services'
        ordering = ['-update_at']


mm_CarService = CarService.objects
