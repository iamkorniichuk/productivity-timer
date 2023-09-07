from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
from rest_framework.serializers import ModelSerializer

from .fields import OnlyPrimaryKeyRelatedField


class DefaultSupportNestedMixin:
    def update_or_create_direct_relations(self, attrs, relations):
        for name, (field, source) in relations.items():
            obj = None

            data = self.get_initial().get(name, None)
            if not data:
                obj = self.fields[name].default(self)
                data = model_to_dict(obj)
            else:
                model_class = field.Meta.model
                pk = self._get_related_pk(data, model_class)
                if pk:
                    obj = model_class.objects.filter(
                        pk=pk,
                    ).first()
            serializer = self._get_serializer_for_field(
                field,
                instance=obj,
                data=data,
            )

            try:
                serializer.is_valid(raise_exception=True)
                attrs[source] = serializer.save(**data)
            except ValidationError as exc:
                raise ValidationError({name: exc.detail})


class IdOrWriteNestedMixin:
    def get_fields(self):
        fields = super().get_fields()
        related_fields = {}
        # TODO: Skip read_only fields
        for name, field in fields.items():
            if isinstance(field, ModelSerializer):
                Model = field.Meta.model
                related_name = name + "_id"
                related_fields[related_name] = OnlyPrimaryKeyRelatedField(
                    Model._default_manager.all()
                )
        fields.update(related_fields)
        return fields
