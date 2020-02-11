#!/usr/bin/env python
# -*- coding: utf-8 -*-
import uuid
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

import datetime
from datetime import date


class Album(models.Model):
    title = models.CharField(max_length=70)
    event_date = models.DateField(default=date.today, blank=True, null=True)
    description = models.TextField(max_length=1024)
    twitter_url = models.URLField(default='', help_text='Link to Twitter Account', blank=True,)
    facebook_url = models.URLField(default='', help_text='Link to Facebook Account', blank=True,)
    flickr_url = models.URLField(default='', help_text='Link to Flick Photo Ablum', blank=True,)
    album_link = models.URLField(help_text='Link to Photo Ablum', blank=False,)
    googlephotos_url = models.URLField(default='', help_text='Link to Google Photo Ablum', blank=True,)
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(600)], format='jpeg', options={'quality': 90})
    tags = models.CharField(max_length=250)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=50, unique=True)

    #def get_absolute_url(self):
    #    return reverse('album', kwargs={'slug':self.slug})

    def __unicode__(self):
        return self.title

class AlbumImage(models.Model):
    image = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(1280)], format='jpeg', options={'quality': 90})
    thumb = ProcessedImageField(upload_to='albums', processors=[ResizeToFit(600)], format='jpeg', options={'quality': 100})
    album = models.ForeignKey('album')
    alt = models.CharField(max_length=255, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    slug = models.SlugField(max_length=70, default=uuid.uuid4, editable=False)