# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django_tables2 import RequestConfig
from django.views.decorators.csrf import csrf_exempt
from .models import Device, Content
from .filters import DeviceFilter, ContentFilter
from .tables import DeviceTable, ContentTable
from .utils import importData


def devices_list(request):
    queryset = Device.objects.select_related().all()
    f = DeviceFilter(request.GET, queryset=queryset)
    table = DeviceTable(f.qs)
    RequestConfig(request, paginate={"per_page": 10, "page": 1}).configure(table)
    return render(request, 'importer/devices_list.html', {'table': table, 'filter': f})

def content_list(request):
    queryset = Content.objects.select_related().all()
    f = ContentFilter(request.GET, queryset=queryset)
    table = ContentTable(f.qs)
    RequestConfig(request, paginate={"per_page": 10, "page": 1}).configure(table)
    return render(request, 'importer/content_list.html', {'table': table, 'filter': f})

@csrf_exempt
def importer(request):
    if request.method == "POST":
        values = request.POST.dict()
        importDevicesSuccess, importContentSuccess, resultDevices, resultContent = importData(values['csv_path'], values['delimiter'])

        errors = ""
        imported = ""

        if importDevicesSuccess:
            imported = resultDevices
        else:
            errors = "FIX ERRORS BEFORE IMPORTING DEVICES:\n" + "\n".join(resultDevices)

        if importContentSuccess:
            imported = imported + (importDevicesSuccess and "\n" or "") + resultContent
        else:
            errors = errors + (not importDevicesSuccess and "\n" or "") + "FIX ERRORS BEFORE IMPORTING CONTENT:\n" + "\n".join(resultContent)

        return render(request, 'importer/importer.html', {'errors': errors, 'imported': imported})
    else:
        return render(request, 'importer/importer.html', {})
