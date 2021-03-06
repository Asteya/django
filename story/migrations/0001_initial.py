# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 22:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause_title', models.CharField(max_length=250)),
                ('cause_cover', models.CharField(max_length=1000)),
                ('body', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Ngo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_name', models.CharField(max_length=500)),
                ('ngo_pic', models.CharField(max_length=1000)),
                ('body', models.CharField(max_length=2000)),
                ('cause', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.Cause')),
            ],
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_title', models.CharField(max_length=250)),
                ('cover', models.CharField(max_length=1000)),
                ('body', models.CharField(max_length=2000)),
                ('cause', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.Cause')),
                ('ngo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.Ngo')),
            ],
        ),
    ]
