from django.db import models
from django.utils.translation import gettext_lazy as _

from commons.models import ShowAnnotationAfterCreateMixin


class PauseManager(ShowAnnotationAfterCreateMixin, models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                is_ended=models.ExpressionWrapper(
                    models.Q(end__isnull=False),
                    output_field=models.BooleanField(_("is ended")),
                ),
                duration=models.ExpressionWrapper(
                    models.F("end") - models.F("start"),  # TODO: Set now if end is null
                    output_field=models.DurationField(_("duration")),
                ),
            )
        )


class Pause(models.Model):
    start = models.DateTimeField(_("start"), auto_now_add=True)
    end = models.DateTimeField(_("end"), null=True, blank=True)
    timer = models.ForeignKey(
        "Timer",
        models.CASCADE,
        related_name="pauses",
        verbose_name=_("timer"),
    )

    objects = PauseManager()

    def __str__(self):
        return str(self.start)
