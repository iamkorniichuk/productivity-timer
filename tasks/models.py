from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from commons.functions import NonAggregateCount

from users.models import User
from themes.models import Theme
from schedules.models import Frequency


class TaskManager(models.Manager):
    def create(self, **kwargs):
        instance = super().create(**kwargs)
        return self.get_queryset().get(pk=instance.pk)

    def get_queryset(self):
        from timers.models import Timer

        related_frequency = Frequency.objects.filter(
            pk=models.OuterRef("task__frequency__pk")
        )[:1]

        related_current_completed_timers = Timer.objects.filter(
            task=models.OuterRef("pk"),
            is_completed=True,
            datetime__range=[
                models.Subquery(related_frequency.values("start")),
                models.Subquery(related_frequency.values("end")),
            ],
        )

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
                completed_timers=models.ExpressionWrapper(
                    models.Subquery(
                        related_current_completed_timers.annotate(
                            count=NonAggregateCount("pk")
                        ).values("count")[:1]
                    ),
                    output_field=models.PositiveIntegerField(_("completed timers")),
                ),
                remaining_timers=models.ExpressionWrapper(
                    models.F("frequency__events_number") - models.F("completed_timers"),
                    output_field=models.IntegerField(_("remaining timers")),
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
    user = models.ForeignKey(
        User,
        models.CASCADE,
        related_name="tasks",
        verbose_name=_("user"),
    )

    objects = TaskManager()

    def get_absolute_url(self):
        return reverse("tasks:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name or str(self.wanted_duration)
