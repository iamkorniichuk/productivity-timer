from django.contrib import admin

from commons.admin import bool_filter_factory

from .models import Theme


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "parent", "user"]
    list_filter = [bool_filter_factory("is_main", title="is main")]
    exclude = []
