from rest_framework.serializers import PrimaryKeyRelatedField


class CurrentUserDefault:
    requires_context = True

    def __call__(self, instance):
        return instance.context["request"].user


class SerializerRepresentationMixin:
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


# TODO: Fix declaring read_only in meta doesn't work for this type
class RepresentativePrimaryKeyRelatedField(
    SerializerRepresentationMixin,
    PrimaryKeyRelatedField,
):
    pass
