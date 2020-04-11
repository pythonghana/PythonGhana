from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django_extensions.db.fields import AutoSlugField
from django_slugify_processor.text import slugify
from django.contrib.contenttypes.fields import GenericRelation
from django.utils.encoding import python_2_unicode_compatible
@python_2_unicode_compatible
 

 
class Book(models.Model):
    book_title = models.CharField(max_length=200)
    book_image = models.ImageField(upload_to='resources/books/',default="team.png")
    book_description = models.TextField(blank=True, help_text="Please enter book description", default="")
    book_link = models.CharField(max_length=100, null=True, blank=True, help_text="Please enter link", default="")
    read_book_link = models.CharField(max_length=100, null=True, blank=True, help_text="Please enter link", default="")
    beginner_level = models.BooleanField(default=False)
    intermediate_level = models.BooleanField(default=False)
    expert_level = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    slug = AutoSlugField(
        populate_from='book_title',
        slugify_function=slugify
    )

    def __str__(self):
        return self.book_title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.book_title)
        return super(Book, self).save(*args, **kwargs)



class Video(models.Model):
    video_title = models.CharField(max_length=200)
    video_release_date = models.CharField(max_length=200, null=True, blank=True,)
    video_speaker = models.CharField(max_length=200, null=True, blank=True,)
    video_image = models.ImageField(upload_to='resources/video/',default="team.png")
    video_author = models.CharField(max_length=200, null=True, blank=True, help_text="Please enter video source, this is where the video is gotten from")
    video_description = models.TextField(blank=True, help_text="Please enter video description", default=" ")
    video_link = models.CharField(max_length=100, null=True, blank=False, help_text="Please enter link", default=" ")
    beginner_level = models.BooleanField(default=False)
    intermediate_level = models.BooleanField(default=False)
    expert_level = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    slug = AutoSlugField(
        populate_from='video_title',
        slugify_function=slugify
    )

    def __str__(self):
        return self.video_title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.video_title)
        return super(Video, self).save(*args, **kwargs)



class Article(models.Model):
    article_title = models.CharField(max_length=200)
    article_image = models.ImageField(upload_to='resources/article/',default="team.png")
    article_author = models.CharField(max_length=200, null=True, blank=True, help_text="Please enter article source, this is where the article is gotten from")
    article_description = models.TextField(blank=True, help_text="Please enter article description", default=" ")
    article_link = models.CharField(max_length=100, null=True, blank=False, help_text="Please enter link", default=" ")
    beginner_level = models.BooleanField(default=False)
    intermediate_level = models.BooleanField(default=False)
    expert_level = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    slug = AutoSlugField(
        populate_from='article_title',
        slugify_function=slugify
    )

    def __str__(self):
        return self.article_title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.article_title)
        return super(Article, self).save(*args, **kwargs)



class Link(models.Model):
    link_title = models.CharField(max_length=200)
    link = models.CharField(max_length=100, null=True, blank=False, help_text="Please enter link", default=" ")
    created_date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    slug = AutoSlugField(
        populate_from='link_title',
        slugify_function=slugify
    )

    def __str__(self):
        return self.link_title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.link_title)
        return super(Link, self).save(*args, **kwargs)
