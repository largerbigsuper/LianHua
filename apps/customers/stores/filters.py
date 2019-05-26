from django_filters import rest_framework as filters

from datamodels.stores.models import mm_Store


class StoreFilter(filters.FilterSet):
    class Meta:
        model = mm_Store.model
        fields = {
            'name': ['contains'],
            'address_info': ['contains'],
            'tags': ['exact'],
            'owner': ['exact'],
            'area': ['exact'],
        }