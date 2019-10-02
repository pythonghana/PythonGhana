# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-02-17 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190217_1005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='url',
        ),
        migrations.AddField(
            model_name='album',
            name='twitter_url',
            field=models.URLField(blank=True, default='', help_text='Link to Twitter Account'),
        ),
        migrations.AlterField(
            model_name='album',
            name='facebook_url',
            field=models.URLField(blank=True, default='', help_text='Link to Facebook Account'),
        ),
    ]