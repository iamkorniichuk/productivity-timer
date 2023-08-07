from django.contrib import admin

from commons.admin import GeneralBooleanListFilter

from .models import Task


class IsDraftListFilter(GeneralBooleanListFilter):
    title = "is draft"
    parameter_name = "is_draft"


class IsDisposableListFilter(GeneralBooleanListFilter):
    title = "is disposable"
    parameter_name = "is_disposable"


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "wanted_duration", "theme", "frequency"]
    list_filter = [IsDraftListFilter, IsDisposableListFilter]
    exclude = []
