from .models import Device, Content
from os import listdir
from os.path import isfile, join
from datetime import datetime
from dateutil import parser

import csv
import io
import logging
import pytz
import sys

logger = logging.getLogger('django')

def importDevices(file_path, delimiter):
    errors = []
    rownum = 0

    file_reader = csv.reader(open(file_path), quotechar='"', delimiter=str(delimiter), quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in file_reader:
        rownum += 1
        error = False

        #test number of columns
        if len(row) != 6:
            errors.append('Wrong number of columns in devices row %s (length: %s)' % (str(rownum), len(row)))
            error = True

        #check date format
        try:
            expire_date = parser.parse(row[4])
        except Exception as e:
            errors.append('Wrong expire date format in devices row %s (%s)' % (str(rownum), str(e)))
            error = True

        #check device status
        if len(row) == 6:
            if row[5] not in [x[0] for x in Device.STATUS_CHOICES]:
                errors.append('Wrong status in devices row %s (%s)' % (str(rownum), str(row[5])))
                error = True

        if error:
            continue

        deviceData = {
            "name": row[1],
            "description": row[2],
            "code": row[3],
            "expire_date": expire_date,
            "status": row[5].strip()
        }

        try:
            device, created = Device.objects.update_or_create(id=row[0], defaults=deviceData)
            if not created:
                Device.objects.filter(id=row[0]).update(date_updated=datetime.utcnow().replace(tzinfo=pytz.utc))
        except Exception as e:
            errors.append('Errow while importing devices row %s (%s)' % (str(rownum), str(e)))
            continue
                              
    if len(errors) > 0:
        logger.error("\n".join(errors))
        return False, errors
    else:
        message = "Succesfully processed %s device rows!" % str(rownum)
        logger.info(message)
        return True, message

def importContent(file_path, delimiter):
    errors = []
    rownum = 0

    file_reader = csv.reader(open(file_path), quotechar='"', delimiter=str(delimiter), quoting=csv.QUOTE_ALL, skipinitialspace=True)
    for row in file_reader:
        rownum += 1
        error = False

        #test number of columns
        if len(row) != 6:
            errors.append('Wrong number of columns in content row %s (length: %s)' % (str(rownum), len(row)))
            error = True

        #check date format
        try:
            expire_date = parser.parse(row[4])
        except Exception as e:
            errors.append('Wrong expire date format in devices row %s (%s)' % (str(rownum), str(e)))
            error = True

        #check content status
        if len(row) == 6:
            if row[5] not in [x[0] for x in Content.STATUS_CHOICES]:
                errors.append('Wrong status in devices row %s (%s)' % (str(rownum), str(row[5])))
                error = True

        if error:
            continue

        try:
            contentData = {
                "name": row[1],
                "description": row[2],
                "device": Device.objects.get(id=row[3]),
                "expire_date": expire_date,
                "status": row[5].strip()
            }      
                  
            content, created = Content.objects.update_or_create(id=row[0], defaults=contentData)
            if not created:
                Content.objects.filter(id=row[0]).update(date_updated=datetime.utcnow().replace(tzinfo=pytz.utc))
        except Exception as e:
            errors.append('Errow while importing content row %s (%s)' % (str(rownum), str(e)))
            continue

    if len(errors) > 0:
        logger.error("\n".join(errors))
        return False, errors
    else:
        message = "Succesfully processed %s content rows!" % str(rownum)
        logger.info(message)
        return True, message         

def importData(csv_path, delimiter):
    files = [f for f in listdir(csv_path) if isfile(join(csv_path, f))]

    if 'devices.csv' in files:
        importDevicesSuccess, resultDevices = importDevices(csv_path + '/devices.csv', delimiter)
    if 'content.csv' in files:
        importContentSuccess, resultContent = importContent(csv_path + '/content.csv', delimiter)

    return importDevicesSuccess, importContentSuccess, resultDevices, resultContent