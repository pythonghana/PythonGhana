# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-02-11 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_remove_team_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='is_advisory_board',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='job_description',
            field=models.CharField(blank=True, default=' ', help_text='Please enter current position and organization working in', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='team',
            name='summarize_biography',
            field=models.TextField(blank=True, default=' ', help_text='Please enter bio of the advisory board member'),
        ),
    ]
