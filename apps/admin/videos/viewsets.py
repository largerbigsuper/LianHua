from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets

from datamodels.videos.models import mm_Video

from apps.admin.videos.serilizers import AdminVideoSerializer
from apps.admin.videos.filters import AdminVideoFilter

class AdminVideoViewSet(viewsets.ModelViewSet):

    permission_classes = [IsAdminUser, IsAuthenticated]
    queryset = mm_Video.all()
    serializer_class = AdminVideoSerializer
    filter_class = AdminVideoFilter