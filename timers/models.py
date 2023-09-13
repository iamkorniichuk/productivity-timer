from django.db import models
from django.db.models import functions
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from commons.models import ShowAnnotationAfterCreateMixin
from commons.functions import NonAggregateSum

from users.models import User
from tasks.models import Task


class TimerManager(ShowAnnotationAfterCreateMixin, models.Manager):
    def get_queryset(self):
        all_ended_related_pauses = Pause.objects.filter(
            timer=models.OuterRef("pk"),
            is_ended=True,
        )

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
                pauses_duration=models.ExpressionWrapper(
                    models.Subquery(
                        all_ended_related_pauses.annotate(
                            sum=NonAggregateSum("duration")
                        ).values("sum")[:1]
                    ),
                    output_field=models.DurationField(_("pauses duration")),
                ),
                # TODO: To test
                duration=models.ExpressionWrapper(
                    models.F("end") - models.F("start") - models.F("pauses_duration"),
                    output_field=models.DurationField(_("duration")),
                ),
                overflow_duration=models.ExpressionWrapper(
                    models.F("duration") - models.F("task__wanted_duration"),
                    output_field=models.DurationField(_("overflow duration")),
                ),
                is_datetime_set=models.ExpressionWrapper(
                    models.Q(set_datetime__isnull=False),
                    output_field=models.BooleanField(_("is datetime set")),
                ),
                is_ended=models.ExpressionWrapper(
                    models.Q(end__isnull=False),
                    output_field=models.BooleanField(_("is ended")),
                ),
                is_completed=models.ExpressionWrapper(
                    models.Q(duration__gte=models.F("task__wanted_duration")),
                    output_field=models.BooleanField(_("is completed")),
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
    user = models.ForeignKey(
        User,
        models.CASCADE,
        related_name="timers",
        verbose_name=_("user"),
    )

    objects = TimerManager()

    def get_absolute_url(self):
        return reverse("timers:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.start)


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
