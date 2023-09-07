from drf_writable_nested.serializers import WritableNestedModelSerializer

from .mixins import DefaultSupportNestedMixin, IdOrWriteNestedMixin


class DefaultSupportNestedSerializer(
    DefaultSupportNestedMixin,
    IdOrWriteNestedMixin,
    WritableNestedModelSerializer,
):
    pass
