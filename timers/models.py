from django.db import models
from django.db.models import functions
from django.utils.translation import gettext_lazy as _


class TimerManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                is_date_set=models.ExpressionWrapper(
                    models.Q(set_date__isnull=False),
                    output_field=models.BooleanField(_("is date set")),
                ),
                actual_date=models.ExpressionWrapper(
                    models.F("start__date"),
                    output_field=models.DateField(
                        _("actual date"),
                    ),
                ),
                date=models.ExpressionWrapper(
                    functions.Coalesce(
                        models.F("set_date"),
                        models.F("actual_date"),
                    ),
                    output_field=models.DateField(
                        _("date"),
                    ),
                ),
                is_ended=models.ExpressionWrapper(
                    models.Q(end__isnull=False),
                    output_field=models.BooleanField(_("is ended")),
                ),
                duration=models.ExpressionWrapper(
                    models.F("end") - models.F("start"),
                    output_field=models.DurationField(_("duration")),
                ),
            )
        )


class Timer(models.Model):
    start = models.DateTimeField(_("start"), auto_now_add=True)
    end = models.DateTimeField(_("end"), null=True, blank=True)
    set_date = models.DateField(_("set date"), null=True, blank=True)

    objects = TimerManager()

    def __str__(self):
        return str(self.start)
