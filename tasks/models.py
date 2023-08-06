from django.db import models
from django.utils.translation import gettext_lazy as _

from themes.models import Theme


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

    def __str__(self):
        return self.name or str(self.wanted_duration)
