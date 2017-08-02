# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
                ('expire_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('EN', 'enabled'), ('DS', 'disabled'), ('DL', 'deleted')], default='D', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('code', models.CharField(max_length=30)),
                ('date_created', models.DateTimeField()),
                ('date_updated', models.DateTimeField()),
                ('expire_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('EN', 'enabled'), ('DS', 'disabled'), ('DL', 'deleted')], default='D', max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='importer.device'),
        ),
    ]