from django.contrib import admin
from . import models


@admin.register(models.Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'manual_order']
    list_editable = ['manual_order']
    ordering = ['manual_order']


@admin.register(models.Framework)
class FrameworksAdmin(admin.ModelAdmin):
    list_display = ['name', 'language']
    list_editable = ['language']


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'language', 'framework']
    prepopulated_fields = {
        'slug': ['title']
    }
    list_editable = ['sub_title']