from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "wanted_duration", "theme"]
    exclude = []
