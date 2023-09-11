from rest_framework.serializers import PrimaryKeyRelatedField


class CurrentUserDefault:
    requires_context = True

    def __call__(self, instance):
        return instance.context["request"].user


class SerializeAnnotationsMixin:
    manager_name = "_default_manager"

    def get_fields(self):
        fields = super().get_fields()
        for name, annotation in self.get_manager_annotations().items():
            fields[name] = self.create_field(annotation)
        return fields

    def create_field(self, annotation):
        serializer_class = self.serializer_field_mapping[
            annotation.output_field.__class__
        ]
        return serializer_class(required=False, read_only=True)

    def get_manager_annotations(self):
        if not hasattr(self, "annotations"):
            objects = getattr(self.Meta.model, self.manager_name).get_queryset()
            self.annotations = objects._query.annotations
        return self.annotations


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
