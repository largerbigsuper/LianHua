from rest_framework import serializers

from datamodels.videos.models import mm_Video


class AdminVideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = mm_Video.model
        fields = ('id', 'name', 'image', 'uri', 'status', 'update_at', 'create_at', 'view_count')
