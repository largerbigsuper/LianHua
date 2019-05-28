from django_filters import rest_framework as filters

from datamodels.videos.models import mm_Video


class VideoFilter(filters.FilterSet):

    class Meta:
        model = mm_Video.model
        fields = {
            'name': ['contains'],
        }