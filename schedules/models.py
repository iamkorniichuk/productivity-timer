from django.db import models
from django.db.models import functions
from django.utils.translation import gettext_lazy as _

from .functions import StartOf, EndOf


class FrequencyManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                start=models.ExpressionWrapper(
                    StartOf(
                        models.F("time_unit"),
                        functions.Now(),
                    ),
                    output_field=models.DateTimeField(_("start")),
                ),
                end=models.ExpressionWrapper(
                    EndOf(
                        models.F("time_unit"),
                        functions.Now(),
                    ),
                    output_field=models.DateTimeField(_("end")),
                ),
                remaining_time=models.ExpressionWrapper(
                    models.F("end") - functions.Now(),
                    output_field=models.DurationField(_("remaining time")),
                ),
                duration=models.ExpressionWrapper(
                    models.F("end") - models.F("start"),
                    output_field=models.DurationField(_("duration")),
                ),
            )
        )


class TimeUnitChoices(models.TextChoices):
    DAY = "day", _("day")
    WEEK = "week", _("week")
    MONTH = "month", _("month")
    QUARTER = "quarter", _("quarter")
    YEAR = "year", _("year")


class Frequency(models.Model):
    events_number = models.PositiveIntegerField(_("events number"))
    time_unit = models.CharField(
        _("time unit"), max_length=32, choices=TimeUnitChoices.choices
    )

    objects = FrequencyManager()

    def __str__(self):
        return f"{self.events_number} per {self.time_unit}"

    class Meta:
        verbose_name_plural = "frequencies"
