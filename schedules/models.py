from django.db import models
from django.utils.translation import gettext_lazy as _


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

    def __str__(self):
        return f"{self.events_number} per {self.time_unit}"

    class Meta:
        verbose_name_plural = "frequencies"
