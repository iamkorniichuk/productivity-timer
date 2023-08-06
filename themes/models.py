from django.db import models
from django.utils.translation import gettext_lazy as _


class ThemeManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                is_main=models.ExpressionWrapper(
                    models.Q(parent__isnull=True),
                    output_field=models.BooleanField(_("is main")),
                )
            )
        )


class Theme(models.Model):
    name = models.CharField(_("name"), max_length=64)
    parent = models.ForeignKey(
        "themes.Theme",
        models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name=_("parent"),
    )

    objects = ThemeManager()

    def __str__(self):
        return self.name
