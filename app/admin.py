from django.contrib import admin
from app.models import BlogPost, BlogPostee
from django.db import models
from django import forms


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'pub_date',)
    prepopulated_fields = {'slug': ('title',)}


class BlogPosteeAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'pub_date',)
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogPostee, BlogPosteeAdmin)




