from django.contrib import admin

from .models import About


admin.site.register(About)

class AboutAdmin(admin.ModelAdmin):
    list_display = ("full_name")
    list_filter = ("full_name")
