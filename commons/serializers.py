from rest_framework.serializers import PrimaryKeyRelatedField


class CurrentUserDefault:
    requires_context = True

    def __call__(self, instance):
        return instance.context["request"].user


class SerializeAnnotationsMixin:
    """
    Implicitly adds manager's annotations. Calls to db once to retrieve all annotation fields.

    Override `queryset` or `.get_queryset()` to set source of annotations different from default model's manager.
    """

    queryset = None

    def get_fields(self):
        fields = super().get_fields()
        for name, annotation in self.get_annotations().items():
            fields[name] = self.create_field(annotation)
        return fields

    def create_field(self, annotation):
        serializer_class = self.serializer_field_mapping[
            annotation.output_field.__class__
        ]
        return serializer_class(required=False, read_only=True)

    def get_queryset(self):
        return self.queryset or self.Meta.model._default_manager.all()

    def get_annotations(self):
        if not hasattr(self, "annotations"):
            self.annotations = self.get_queryset()._query.annotations
        return self.annotations


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
