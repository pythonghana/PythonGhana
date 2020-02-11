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
 

 
class Team(models.Model):
    team_name = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to='teams/',default="team.png")
    position = models.CharField(max_length=200, blank=True,  help_text="Position of the team eg. CEO",default="")
    twitter = models.CharField(max_length=100, null=True, blank=True, help_text="Please enter only the user name eg.'mawy_7' ", default=" ")
    linkedin = models.CharField(max_length=100, null=True, blank=True, help_text="Please enter only the user name eg. in/mawy7 ", default=" ")
    created_date = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    is_current_lead = models.BooleanField(default=False)
    is_past_lead = models.BooleanField(default=False)
    is_advisory_board = models.BooleanField(default=False)
    job_description = models.CharField(max_length=100, null=True, blank=True, help_text="Please enter current position and organization working in", default=" ")
    summarize_biography = models.TextField(blank=True, help_text="Please enter bio of the advisory board member", default=" ")
    slug = AutoSlugField(
        populate_from='team_name',
        slugify_function=slugify
    )

    def __str__(self):
        return self.team_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.team_name)
        return super(Team, self).save(*args, **kwargs)