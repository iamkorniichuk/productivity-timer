from rest_framework.serializers import PrimaryKeyRelatedField, URLField


class CurrentUserDefault:
    requires_context = True

    def __call__(self, instance):
        return instance.context["request"].user


class SerializeUrlMixin:
    """
    Populates serializer with URL field.

    Override `url_source` to specify a source different from `.get_absolute_url()`.
    """

    url_source = "get_absolute_url"

    def get_fields(self):
        fields = super().get_fields()
        fields["url"] = URLField(source=self.url_source, read_only=True)
        return fields


# TODO: Fix declaring read_only in meta doesn't work for this type
class RepresentativePrimaryKeyRelatedField(PrimaryKeyRelatedField):
    """
    Behaves as `PrimaryKeyRelatedField` but returns representation of specified serializer.

    Override `queryset` or `.get_queryset()` to set source of retrieving an object different from default model's manager.
    """

    def __init__(self, serializer_class, *args, **kwargs):
        self.serializer_class = serializer_class
        self.queryset = kwargs.pop("queryset", None)
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        return self.queryset or self.serializer_class.Meta.model._default_manager.all()

    def to_representation(self, value):
        pk = super().to_representation(value)
        obj = self.get_queryset().get(pk=pk)
        serializer = self.serializer_class()
        return serializer.to_representation(obj)
