from rest_framework.serializers import PrimaryKeyRelatedField


class CurrentUserDefault:
    requires_context = True

    def __call__(self, instance):
        return instance.context["request"].user


class SerializerRepresentationMixin:
    def __init__(self, serializer_class, queryset=None, *args, **kwargs):
        self.serializer_class = serializer_class
        super().__init__(*args, **kwargs)
        self._queryset = queryset

    def get_queryset(self):
        return self._queryset or self.serializer_class.Meta.model._default_manager.all()

    def to_representation(self, pk):
        data = {"pk": str(pk)}  # TODO: To refactor
        obj = self.get_queryset().get(**data)
        serializer = self.serializer_class()
        a = serializer.to_representation(obj)
        return a


# TODO: Fix declaring read_only in meta doesn't work for this type
class RepresentativePrimaryKeyRelatedField(
    SerializerRepresentationMixin,
    PrimaryKeyRelatedField,
):
    pass
