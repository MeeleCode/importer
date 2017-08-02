import django_tables2 as tables
from .models import Device
from .models import Content

class DeviceTable(tables.Table):
    class Meta:
        model = Device
        attrs = {'class': 'paleblue'}

class ContentTable(tables.Table):
    class Meta:
        model = Content
        attrs = {'class': 'paleblue'}
