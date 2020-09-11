# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-04-11 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='beginner_level',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='expert_level',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='intermediate_level',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='beginner_level',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='expert_level',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='intermediate_level',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='beginner_level',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='expert_level',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='video',
            name='intermediate_level',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_source',
            field=models.CharField(blank=True, help_text='Please enter article source, this is where the article is gotten from', max_length=200, null=True),
        ),
    ]