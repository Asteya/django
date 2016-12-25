# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0005_auto_20161222_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='ngo',
            name='address',
            field=models.CharField(max_length=500, null='true'),
        ),
        migrations.AddField(
            model_name='ngo',
            name='awards',
            field=models.CharField(max_length=1000, null='true'),
        ),
        migrations.AddField(
            model_name='ngo',
            name='contact',
            field=models.CharField(max_length=500, null='true'),
        ),
        migrations.AddField(
            model_name='ngo',
            name='founded_date',
            field=models.DateField(null='true'),
        ),
        migrations.AddField(
            model_name='ngo',
            name='history',
            field=models.CharField(max_length=2000, null='true'),
        ),
        migrations.AddField(
            model_name='ngo',
            name='mission',
            field=models.CharField(max_length=1000, null='true'),
        ),
        migrations.AddField(
            model_name='ngo',
            name='ngo_cover',
            field=models.FileField(default=12, upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ngo',
            name='vision',
            field=models.CharField(max_length=1000, null='true'),
        ),
        migrations.AddField(
            model_name='ngo',
            name='website',
            field=models.CharField(max_length=200, null='true'),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='body',
            field=models.CharField(max_length=2000, null='true'),
        ),
    ]