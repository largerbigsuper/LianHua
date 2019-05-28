from django_filters import rest_framework as filters

from datamodels.products.models import mm_Product

class AdminProductFilter(filters.FilterSet):
    class Meta:
        model = mm_Product.model
        fields = {
            'name': ['contains'],
            'store': ['exact'],
            'types': ['exact'],
            'price': ['gt', 'lt'],
        }