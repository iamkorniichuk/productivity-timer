from django.db import models
from django.utils.translation import gettext_lazy as _

from themes.models import Theme
from schedules.models import Frequency


class TaskManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                is_draft=models.ExpressionWrapper(
                    models.Q(theme__isnull=True),
                    output_field=models.BooleanField(_("is draft")),
                ),
                is_disposable=models.ExpressionWrapper(
                    models.Q(frequency__isnull=True),
                    output_field=models.BooleanField(_("is disposable")),
                ),
            )
        )


class Task(models.Model):
    name = models.CharField(
        _("name"),
        max_length=64,
        null=True,
        blank=True,
    )
    wanted_duration = models.DurationField(_("wanted duration"))
    theme = models.ForeignKey(
        Theme,
        models.CASCADE,
        null=True,
        blank=True,
        related_name="tasks",
        verbose_name=_("theme"),
    )
    frequency = models.ForeignKey(
        Frequency,
        models.CASCADE,
        null=True,
        blank=True,
        related_name="tasks",
        verbose_name=_("frequency"),
    )

    objects = TaskManager()

    def __str__(self):
        return self.name or str(self.wanted_duration)
