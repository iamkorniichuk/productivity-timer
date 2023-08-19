from django.contrib import admin

from commons.admin import bool_filter_factory

from .models import Timer


@admin.register(Timer)
class TimerAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "start",
        "date",
        "task",
        "duration",
        "actual_date",
    ]
    list_filter = [
        bool_filter_factory("is_ended", title="is ended"),
        bool_filter_factory("is_date_set", title="is date set"),
        bool_filter_factory("is_disposable", title="is disposable"),
    ]
    date_hierarchy = "start"
    exclude = []

    def duration(self, obj):
        return obj.duration

    def actual_date(self, obj):
        return obj.actual_date

    def date(self, obj):
        return obj.date
