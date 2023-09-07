from rest_framework.serializers import PrimaryKeyRelatedField


class OnlyPrimaryKeyRelatedField(PrimaryKeyRelatedField):
    def __init__(self, queryset, **kwargs):
        kwargs["queryset"] = queryset
        kwargs["required"] = False
        kwargs["write_only"] = True
        super().__init__(**kwargs)

    def to_internal_value(self, data):
        return super().to_internal_value(data).pk
