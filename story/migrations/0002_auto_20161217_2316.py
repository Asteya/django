# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='cover',
            field=models.FileField(upload_to=b''),
        ),
    ]