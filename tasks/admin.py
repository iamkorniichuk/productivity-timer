from django.contrib import admin

from commons.admin import bool_filter_factory

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "name",
        "wanted_duration",
        "theme",
        "frequency",
        "completed_timers",
        "remaining_timers",
        "user",
    ]
    list_filter = [
        bool_filter_factory("is_disposable", title="is disposable"),
        bool_filter_factory("is_draft", title="is draft"),
    ]
    exclude = []

    def completed_timers(self, obj):
        return obj.completed_timers

    def remaining_timers(self, obj):
        return obj.remaining_timers
