from django_filters import rest_framework as fliters

from datamodels.videos.models import Video


class AdminVideoFilter(fliters.FilterSet):

    class Meta:
        model = Video
        fields = {
            'name': ['contains'],
            'status': ['exact'],
        }