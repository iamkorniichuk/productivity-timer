from django.core.exceptions import ValidationError
from django.forms.models import model_to_dict
from drf_writable_nested.mixins import BaseNestedModelSerializer


class DefaultSupportNestedMixin(BaseNestedModelSerializer):
    def update_or_create_direct_relations(self, attrs, relations):
        for field_name, (field, field_source) in relations.items():
            obj = None

            data = self.get_initial().get(field_name, None)
            if not data:
                obj = self.fields[field_name].default(self)
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
                attrs[field_source] = serializer.save(**data)
            except ValidationError as exc:
                raise ValidationError({field_name: exc.detail})
