from django.contrib import admin

from commons.admin import GeneralBooleanListFilter

from .models import Theme


class IsMainListFilter(GeneralBooleanListFilter):
    title = "is main"
    parameter_name = "is_main"


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "parent"]
    list_filter = [IsMainListFilter]
    exclude = []
