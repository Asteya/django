# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-22 00:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0004_ngo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='ngo_pic',
            field=models.FileField(upload_to=b''),
        ),
    ]