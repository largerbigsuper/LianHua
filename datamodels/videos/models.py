from django.db import models

from LianHua.settings import DB_PREFIX
from lib.modelmanager import ModelManager, BaseModel


class VideoManager(ModelManager):
    
    def published_videos(self):
        return self.filter(status=ModelManager.VIDEO_STATUS_PUBLISHED)

    def update_view_count(self, pk, amont=1):
        """更新访问量"""
        self.filter(pk=pk).update(view_count=amont)


class Video(BaseModel):

    name = models.CharField(max_length=100, db_index=True, verbose_name='视频名称')
    image = models.CharField(max_length=200, verbose_name='封面图')
    uri = models.CharField(max_length=200, verbose_name='视频地址')
    status = models.PositiveSmallIntegerField(choices=ModelManager.VIDEO_STATUS_CHOICE,
                                              default=ModelManager.VIDEO_STATUS_UNPUBLISHED,
                                              verbose_name='未发布|已发布'
                                              )
    view_count = models.PositiveIntegerField(default=0, verbose_name='观看次数')

    objects = VideoManager()

    class Meta:
        db_table = DB_PREFIX + 'videos'
        ordering = ['-id']


mm_Video = Video.objects
