from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers
from drf_annotations.mixins import SerializeAnnotationsMixin

from commons.serializers import SerializeUrlMixin

from .models import Pause


class ContentTypeField(serializers.PrimaryKeyRelatedField):
    def use_pk_only_optimization(self):
        return False

    def __init__(self, **kwargs):
        kwargs["queryset"] = ContentType.objects.all()
        super().__init__(**kwargs)

    def to_internal_value(self, data):
        instance = self.queryset.get(model=data)
        return super().to_internal_value(instance.pk)

    def to_representation(self, value):
        return value.model


class PauseSerializer(
    SerializeAnnotationsMixin,
    SerializeUrlMixin,
    serializers.ModelSerializer,
):
    class Meta:
        model = Pause
        fields = "__all__"

    content_type = ContentTypeField()
