from django.contrib import admin
from .models import Book, Video, Article, Link
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ("book_title","created_date")
    list_filter = ("book_title","created_date")


class VideoAdmin(admin.ModelAdmin):
    list_display = ("video_title","created_date")
    list_filter = ("video_title","created_date")


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("article_title","created_date")
    list_filter = ("article_title","created_date")


class LinkAdmin(admin.ModelAdmin):
    list_display = ("link_title","created_date")
    list_filter = ("link_title","created_date")

admin.site.register(Book, BookAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Article, ArticleAdmin)
