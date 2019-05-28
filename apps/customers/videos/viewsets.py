from rest_framework import viewsets
from rest_framework import status

from LianHua.settings import CID
from datamodels.videos.models import mm_Video
from datamodels.data.models import mm_CustomerAccessVideoRecord
from apps.customers.videos.serializers import VideoSerializer
from apps.customers.videos.filters import VideoFilter



class VideoViewSet(viewsets.ReadOnlyModelViewSet):
    
    permission_classes = []
    queryset = mm_Video.published_videos()
    serializer_class = VideoSerializer
    filter_class = VideoFilter

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            mm_CustomerAccessVideoRecord.add_record(request.session[CID], kwargs['pk'])
            mm_Video.update_view_count(kwargs['pk'])
        return response
