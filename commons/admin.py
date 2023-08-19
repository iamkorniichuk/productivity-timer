from django.contrib import admin


def bool_filter_factory(parameter_name, **kwargs):
    body = {
        "parameter_name": parameter_name,
    }
    body.update(kwargs)
    list_filter = type("BoolFilter", (GeneralBooleanListFilter,), body)

    return list_filter


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
