from  django.contrib import admin
from  .models import Team

admin.site.register(Team)

class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('team_name',)}