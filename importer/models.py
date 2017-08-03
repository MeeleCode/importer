# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Device(models.Model):
    STATUS_CHOICES = (
        ('enabled', 'Enabled'),
        ('disabled', 'Disabled'),
        ('deleted', 'Deleted')
    )

    name = models.CharField(max_length=32)
    description = models.TextField()
    code = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(blank=True, null=True)
    expire_date = models.DateTimeField()
    status = models.CharField(
        max_length = 8,
        choices = STATUS_CHOICES,
        default = 'disabled',
    )

    def __str__(self):
        return self.name

class Content(models.Model):
    STATUS_CHOICES = (
        ('enabled', 'Enabled'),
        ('disabled', 'Disabled'),
        ('deleted', 'Deleted')
    )

    name = models.CharField(max_length=32)
    description = models.TextField()
    device = models.ForeignKey(
        'Device',
        on_delete=models.CASCADE,
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(blank=True, null=True)
    expire_date = models.DateTimeField()
    status = models.CharField(
        max_length = 8,
        choices = STATUS_CHOICES,
        default = 'disabled',
    )

    def __str__(self):
        return self.name
