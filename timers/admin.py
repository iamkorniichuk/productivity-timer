from django.contrib import admin

from commons.admin import GeneralBooleanListFilter

from .models import Timer


class IsEndedListFilter(GeneralBooleanListFilter):
    title = "is ended"
    parameter_name = "is_ended"


class IsDateSetListFilter(GeneralBooleanListFilter):
    title = "is date set"
    parameter_name = "is_date_set"


@admin.register(Timer)
class TimerAdmin(admin.ModelAdmin):
    list_display = [
        "pk",
        "start",
        "date",
        "duration",
        "actual_date",
    ]
    list_filter = [IsEndedListFilter, IsDateSetListFilter]
    date_hierarchy = "start"
    exclude = []

    def duration(self, obj):
        return obj.duration

    def actual_date(self, obj):
        return obj.actual_date

    def date(self, obj):
        return obj.date
