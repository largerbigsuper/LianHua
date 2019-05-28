from rest_framework import serializers

from datamodels.videos.models import mm_Video


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = mm_Video.model
        fields = ('id', 'name', 'image', 'uri', 'create_at', 'view_count')
