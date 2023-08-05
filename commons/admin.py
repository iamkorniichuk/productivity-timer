from django.contrib import admin


class GeneralBooleanListFilter(admin.SimpleListFilter):
    def lookups(self, *args, **kwargs):
        return [
            (True, "True"),
            (False, "False"),
        ]

    def queryset(self, request, queryset):
        value = self.value()
        if value:
            return queryset.filter(**{self.parameter_name: value})
        return queryset
