from django.contrib import admin

from commons.utils import format_timedelta

from .models import Frequency


@admin.register(Frequency)
class FrequencyAdmin(admin.ModelAdmin):
    list_display = ["pk", "events_number", "duration", "start", "end", "remaining_time"]
    list_filter = [("time_unit", admin.filters.ChoicesFieldListFilter)]
    exclude = []

    def start(self, obj):
        return obj.start

    start.admin_order_field = "start"

    def end(self, obj):
        return obj.end

    end.admin_order_field = "end"

    def duration(self, obj):
        return format_timedelta(obj.duration, "{d} days")

    duration.admin_order_field = "duration"

    def remaining_time(self, obj):
        return format_timedelta(obj.remaining_time)

    remaining_time.admin_order_field = "remaining_time"
