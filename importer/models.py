# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Device(models.Model):
    STATUS_CHOICES = (
        ('EN', 'enabled'),
        ('DS', 'disabled'),
        ('DL', 'deleted')
    )

    name = models.CharField(max_length=32)
    description = models.TextField()
    code = models.CharField(max_length=30)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    expire_date = models.DateTimeField()
    status = models.CharField(
        max_length = 2,
        choices = STATUS_CHOICES,
        default = 'D',
    )

    def publish(self):
        self.date_created = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Content(models.Model):
    STATUS_CHOICES = (
        ('EN', 'enabled'),
        ('DS', 'disabled'),
        ('DL', 'deleted')
    )

    name = models.CharField(max_length=32)
    description = models.TextField()
    device = models.ForeignKey(
        'Device',
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    expire_date = models.DateTimeField()
    status = models.CharField(
        max_length = 2,
        choices = STATUS_CHOICES,
        default = 'D',
    )   

    def publish(self):
        self.date_created = timezone.now()
        self.save()

    def __str__(self):
        return self.name
