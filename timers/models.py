from django.db import models
from django.db.models import functions
from django.utils.translation import gettext_lazy as _


from tasks.models import Task


class TimerManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                datetime=models.ExpressionWrapper(
                    functions.Coalesce(
                        models.F("set_datetime"),
                        models.F("start"),
                    ),
                    output_field=models.DateTimeField(
                        _("datetime"),
                    ),
                ),
                duration=models.ExpressionWrapper(
                    models.F("end") - models.F("start"),
                    output_field=models.DurationField(_("duration")),
                ),
                is_datetime_set=models.ExpressionWrapper(
                    models.Q(set_datetime__isnull=False),
                    output_field=models.BooleanField(_("is datetime set")),
                ),
                is_going=models.ExpressionWrapper(
                    models.Q(end__isnull=True),
                    output_field=models.BooleanField(_("is going")),
                ),
                is_disposable=models.ExpressionWrapper(
                    models.Q(task__isnull=True),
                    output_field=models.BooleanField(_("is disposable")),
                ),
                is_completed=models.ExpressionWrapper(
                    models.Q(duration__gte=models.F("task__wanted_duration")),
                    output_field=models.BooleanField(_("is completed")),
                ),
            )
        )


class CurrentTimerManage(TimerManager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(
                datetime__range=(
                    models.F("task__frequency__start"),
                    models.F("task__frequency__end"),
                ),
            )
        )


class Timer(models.Model):
    start = models.DateTimeField(_("start"), auto_now_add=True)
    end = models.DateTimeField(_("end"), null=True, blank=True)
    set_datetime = models.DateTimeField(_("set datetime"), null=True, blank=True)
    task = models.ForeignKey(
        Task,
        models.CASCADE,
        related_name="timers",
        verbose_name=_("task"),
    )

    objects = TimerManager()
    current_objects = CurrentTimerManage()

    def __str__(self):
        return str(self.start)
