from django.db.models import Prefetch
from rest_framework.serializers import BaseSerializer


class UserRelatedObjectsMixin:
    """
    Limit queryset to objects which include FK to current logged in user.

    Override user_field_name to specify user's property in serializer.
    """

    user_field_name = "user"

    def get_queryset(self):
        return super().get_queryset().filter(**self.user_kwargs)

    def perform_create(self, serializer):
        serializer.save(**self.user_kwargs)

    @property
    def user_kwargs(self):
        return {self.user_field_name: self.request.user}


class PrefetchRelatedManagersMixin:
    """
    Prefetch related models which are declared in serializer_class and are inherit from BaseSerializer.

    Override serializer_managers property to set used manager: {field_name: manager_name}.
    """

    serializer_managers = {}

    def get_queryset(self):
        queryset = super().get_queryset()
        serializer = self.serializer_class

        for name, field in serializer._declared_fields.items():
            if isinstance(field, BaseSerializer):
                model = field.Meta.model
                manager = self.serializer_managers.pop(name, "objects")
                queryset = queryset.prefetch_related(
                    Prefetch(name, getattr(model, manager).all())
                )

        return queryset
