from collections.abc import Iterable
from django.db import models
from django.db.models import functions
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class PauseManager(models.Manager):
    def get_queryset(self):
        current_end = functions.Coalesce(models.F("end"), functions.Now())

        return (
            super()
            .get_queryset()
            .annotate(
                is_ended=models.ExpressionWrapper(
                    models.Q(end__isnull=False),
                    output_field=models.BooleanField(_("is ended")),
                ),
                duration=models.ExpressionWrapper(
                    current_end - models.F("start"),
                    output_field=models.DurationField(_("duration")),
                ),
            )
        )


# TODO: Add user?
class Pause(models.Model):
    start = models.DateTimeField(_("start"), auto_now_add=True)
    end = models.DateTimeField(_("end"), null=True, blank=True)
    content_type = models.ForeignKey(
        ContentType,
        models.CASCADE,
        limit_choices_to=models.Q(app_label="timers", model="timer")
        | models.Q(app_label="tasks", model="task"),
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = PauseManager()

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("pauses:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return str(self.start)
