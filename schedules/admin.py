from django.contrib import admin

from .models import Frequency


@admin.register(Frequency)
class FrequencyAdmin(admin.ModelAdmin):
    list_display = ["pk", "events_number", "time_unit"]
    list_filter = [("time_unit", admin.filters.ChoicesFieldListFilter)]
    exclude = []
