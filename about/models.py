from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone
import datetime
from datetime import date

# Create your models here.


class About(models.Model):
    created_date = models.DateField(default=date.today, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='team/',default="team.png")
    full_name = models.CharField(max_length=50, help_text="What is the name of team member")
    twitter_handle = models.CharField(max_length=100, null=True, help_text="Please enter only the user name eg.'mawy_7' ", default="")
    linkedin = models.CharField(max_length=100, null=True, help_text="Please enter only the user name eg. in/mawy7 ", default="")
    position_held = models.CharField(max_length=100, null=True, help_text="Please enter the position held ", default="")
    
    class Meta:
        managed = True

    def __str__(self):
        return str(self.full_name)