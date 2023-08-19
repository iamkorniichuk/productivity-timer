from django.contrib import admin

from commons.admin import GeneralBooleanListFilter
from commons.utils import format_timedelta

from .models import Timer


class IsEndedListFilter(GeneralBooleanListFilter):
    title = "is ended"
    parameter_name = "is_ended"


class IsDateSetListFilter(GeneralBooleanListFilter):
    title = "is date set"
    parameter_name = "is_date_set"


class IsCompletedListFilter(GeneralBooleanListFilter):
    title = "is completed"
    parameter_name = "is_completed"


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
        IsEndedListFilter,
        IsDateSetListFilter,
        IsCompletedListFilter,
    ]
    date_hierarchy = "start"
    exclude = []

    def duration(self, obj):
        return format_timedelta(obj.duration)

    duration.admin_order_field = "duration"

    def datetime(self, obj):
        return obj.datetime

    datetime.admin_order_field = "datetime"
