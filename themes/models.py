from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from commons.models import ShowAnnotationAfterCreateMixin

from users.models import User


class ThemeManager(ShowAnnotationAfterCreateMixin, models.Manager):
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


class MainThemeManager(ThemeManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_main=True)


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
    user = models.ForeignKey(
        User,
        models.CASCADE,
        related_name="themes",
        verbose_name=_("user"),
    )

    objects = ThemeManager()
    main_objects = MainThemeManager()

    def get_absolute_url(self):
        return reverse("themes:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
