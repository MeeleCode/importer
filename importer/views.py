# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Device, Content
from .filters import DeviceFilter, ContentFilter
from .tables import DeviceTable, ContentTable


def devices_list(request):
    queryset = Device.objects.select_related().all()
    f = DeviceFilter(request.GET, queryset=queryset)
    table = DeviceTable(f.qs)
    RequestConfig(request, paginate={"per_page": 30, "page": 1}).configure(table)
    return render(request, 'importer/devices_list.html', {'table': table, 'filter': f})

def content_list(request):
    queryset = Content.objects.select_related().all()
    f = ContentFilter(request.GET, queryset=queryset)
    table = ContentTable(f.qs)
    RequestConfig(request, paginate={"per_page": 30, "page": 1}).configure(table)
    return render(request, 'importer/content_list.html', {'table': table, 'filter': f})

def importer(request):
    import pdb; pdb.set_trace()
    if request.method == "POST":
        if form.is_valid():
            test = 1
            import pdb; pdb.set_trace()       
    return render(request, 'importer/importer.html', {})
