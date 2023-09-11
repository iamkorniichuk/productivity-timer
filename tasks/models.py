from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from commons.functions import NonAggregateCount
from commons.models import ShowAnnotationAfterCreateMixin

from users.models import User
from themes.models import Theme
from schedules.models import Frequency


class TaskManager(ShowAnnotationAfterCreateMixin, models.Manager):
    def get_queryset(self):
        from timers.models import Timer

        related_frequency = Frequency.objects.filter(
            pk=models.OuterRef("task__frequency__pk")
        )[:1]

        all_related_completed_timers = Timer.objects.filter(
            task=models.OuterRef("pk"),
            is_completed=True,
        )

        current_related_completed_timers = all_related_completed_timers.filter(
            datetime__range=[
                models.Subquery(related_frequency.values("start")),
                models.Subquery(related_frequency.values("end")),
            ],
        )

        return (
            super()
            .get_queryset()
            .annotate(
                is_current_version=models.ExpressionWrapper(
                    models.Q(next_version__isnull=True),
                    output_field=models.BooleanField(_("is current version")),
                ),
                is_draft=models.ExpressionWrapper(
                    models.Q(theme__isnull=True),
                    output_field=models.BooleanField(_("is draft")),
                ),
                is_disposable=models.ExpressionWrapper(
                    models.Q(frequency__isnull=True),
                    output_field=models.BooleanField(_("is disposable")),
                ),
                all_completed_timers=models.ExpressionWrapper(
                    models.Subquery(
                        all_related_completed_timers.annotate(
                            count=NonAggregateCount("pk")
                        ).values("count")[:1]
                    ),
                    output_field=models.PositiveIntegerField(_("all completed timers")),
                ),
                current_completed_timers=models.ExpressionWrapper(
                    models.Subquery(
                        current_related_completed_timers.annotate(
                            count=NonAggregateCount("pk")
                        ).values("count")[:1]
                    ),
                    output_field=models.PositiveIntegerField(
                        _("current completed timers")
                    ),
                ),
                remaining_timers=models.ExpressionWrapper(
                    models.F("frequency__events_number")
                    - models.F("current_completed_timers"),
                    output_field=models.IntegerField(_("remaining timers")),
                ),
            )
        )


class CurrentVersionTaskManager(TaskManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_current_version=True)


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
    previous_version = models.OneToOneField(
        "Task",
        models.CASCADE,
        null=True,
        blank=True,
        related_name="next_version",
        verbose_name=_("previous version"),
    )

    objects = TaskManager()
    current_version_objects = CurrentVersionTaskManager()

    def get_absolute_url(self):
        return reverse("tasks:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name or str(self.wanted_duration)
