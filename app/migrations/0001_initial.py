# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2020-02-07 14:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=1024)),
                ('twitter_url', models.URLField(blank=True, default='', help_text='Link to Twitter Account')),
                ('facebook_url', models.URLField(blank=True, default='', help_text='Link to Facebook Account')),
                ('flickr_url', models.URLField(blank=True, default='', help_text='Link to Flick Photo Ablum')),
                ('album_link', models.URLField(help_text='Link to Photo Ablum')),
                ('googlephotos_url', models.URLField(blank=True, default='', help_text='Link to Google Photo Ablum')),
                ('thumb', imagekit.models.fields.ProcessedImageField(upload_to='albums')),
                ('tags', models.CharField(max_length=250)),
                ('is_visible', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='albums')),
                ('thumb', imagekit.models.fields.ProcessedImageField(upload_to='albums')),
                ('alt', models.CharField(default=uuid.uuid4, max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('width', models.IntegerField(default=0)),
                ('height', models.IntegerField(default=0)),
                ('slug', models.SlugField(default=uuid.uuid4, editable=False, max_length=70)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Album')),
            ],
        ),
    ]
