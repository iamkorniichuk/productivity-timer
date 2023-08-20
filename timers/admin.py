from django.contrib import admin

from commons.admin import bool_filter_factory
from commons.utils import format_timedelta

from .models import Timer


@admin.register(Timer)
class TimerAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "start",
        "datetime",
        "task",
        "duration",
    ]
    list_filter = [
        bool_filter_factory("is_datetime_set", title="is datetime set"),
        bool_filter_factory("is_going", title="is going"),
        bool_filter_factory("is_disposable", title="is disposable"),
        bool_filter_factory("is_completed", title="is completed"),
    ]
    date_hierarchy = "start"
    exclude = []

    def duration(self, obj):
        return format_timedelta(obj.duration)

    duration.admin_order_field = "duration"

    def datetime(self, obj):
        return obj.datetime

    datetime.admin_order_field = "datetime"
