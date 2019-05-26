from django_filters import rest_framework as filters

from datamodels.services.models import CarService


class AdminCarServiceFilter(filters.FilterSet):

    class Meta:
        model = CarService
        fields = {
            'car_service_type': ['exact'],
            'range_type': ['exact'],
            'area_from': ['exact'],
            'area_to': ['exact'],
            'area_from_text': ['contains'],
            'area_to_text': ['contains'],
            'start_at': ['lt', 'gt'],
            'site_count': ['lt', 'gt', 'exact'],
        }

