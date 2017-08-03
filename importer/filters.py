import django_filters
from .models import Device
from .models import Content

class DeviceFilter(django_filters.FilterSet):
    class Meta:
        model = Device

        fields = {
            'name': ['icontains'],
            'code': ['icontains'],
            'status': ['exact'],
            'date_created': ['lt', 'gt'],
            'expire_date': ['lt', 'gt']
        }
        order_by = ['name']     

class ContentFilter(django_filters.FilterSet):
    class Meta:
        model = Content

        fields = {
            'name': ['icontains'],
            'status': ['exact'],
            'date_created': ['lt', 'gt'],
            'expire_date': ['lt', 'gt']
        }
        order_by = ['name']